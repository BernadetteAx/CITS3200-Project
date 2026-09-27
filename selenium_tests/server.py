"""Private test server. Run only through the Selenium fixtures, never deploy."""
import os
import sys
from pathlib import Path

# Support the project's gevent installation without blocking its event loop.
try:
    from gevent import monkey
except ImportError:
    pass
else:
    monkey.patch_all()

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from flask import abort, jsonify, request
from app import app
from app.extensions import socketio
from app.sockets.sessions import sessions
from app.sockets.handlers import auction, mission

TOKEN = os.environ['SELENIUM_TEST_TOKEN']
TOOLS = ['Rope', 'Mirror', 'Handheld Radios', 'Ice Axes', 'Water Bottle', 'Fire Starter Kit']


def item(name, index, cost=20):
    return {'id': f'test-item-{index}', 'name': name, 'cost': cost,
            'description': 'Controlled Selenium equipment.',
            'image': 'icons8-tools-32.png', 'hotbar_image': 'icons8-tools-32.png'}


def mission_data():
    data = {'mission': 'Selenium Rescue', 'location': 'Jungle',
            'mission_description': 'A predictable rescue mission for browser testing.'}
    for index, name in enumerate(TOOLS, 1):
        data[f'challenge_{index}'] = {
            'challenge_name': f'Rescue obstacle {index}', 'type': 'Environmental Obstacle',
            'desc': f'Clear rescue obstacle {index}.',
            'items': {name: {'use_desc': f'You use the {name} to clear obstacle {index}.',
                            'point_value': 10, 'point_desc': 'Careful teamwork earns ten points.'}},
            'failure_items': {'Knockout Gas': {
                'use_desc': 'The gas incapacitates the entire rescue team.',
                'point_value': 0, 'point_desc': 'The rescue ends immediately.'}},
        }
    return data


@app.get('/__selenium__/health')
def health():
    return jsonify(ok=True)


@app.post('/__selenium__/seed')
def seed():
    """Arrange starting data only; browser actions still use real application handlers."""
    if request.headers.get('X-Selenium-Token') != TOKEN:
        abort(403)
    payload = request.get_json()
    session = sessions.get(payload['code'])
    if not session or session['phase'] != 'lobby':
        abort(409, 'Seed only a room created through the lobby UI.')
    scenario = payload['scenario']
    if scenario == 'mission':
        session['purchased_items'] = [item(name, i) for i, name in enumerate(TOOLS)]
        session['purchased_items'] += [item('Knockout Gas', 6), item('Spoon', 7)]
        session['generated_mission'] = mission_data()
        mission.initialise_mission(session, session['generated_mission'])
        session['phase'] = 'mission'
    elif scenario == 'auction':
        auction.initialise_auction(session)
        pair = [item('Rope', 0, 100), item('Mirror', 1, 200)]
        state = session['auction']
        state['item_pairs'] = [pair, [item('Water Bottle', 2), item('Ice Axes', 3)]]
        state['budget'] = payload.get('budget', 1000)
        session['phase'] = 'auction'
        auction._start_round(payload['code'], session)
    else:
        abort(400, 'Unknown scenario')
    return jsonify(ok=True)


if __name__ == '__main__':
    kwargs = {'allow_unsafe_werkzeug': True} if socketio.async_mode == 'threading' else {}
    socketio.run(app, host='127.0.0.1', port=int(sys.argv[1]),
                 debug=False, use_reloader=False, **kwargs)
