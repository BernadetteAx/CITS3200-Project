# =====================================================================
# HANDLERS/LOBBY.PY — logic for everything that happens in the lobby
# =====================================================================
#
# WHAT IS A WEBSOCKET, IN PLAIN TERMS?
# A normal web request (loading a page, an API call) is like sending a
# letter and getting one reply back — the connection then closes. A
# WebSocket stays open, and either side (server or browser) can send
# messages down it at any time, in either direction. That's what makes
# it good for games — the server can push "someone else just moved" to
# everyone instantly, instead of everyone having to keep asking "did
# anything change yet?" every second. Flask-SocketIO is a library that
# adds this on top of Flask (which normally only does the
# "letter and one reply" style of request)
#
# THE BIG IDEA OF THIS WHOLE PROJECT:
# The server is the ONE source of truth for what's happening in a game.
# Browsers (clients) NEVER decide game outcomes themselves — they just
# say "I'd like to do X" and the server decides whether that's allowed,
# updates its own copy of the game state, and then tells EVERYONE in
# that session what the new state is
#
#   Client:  "I want to ready up"  -->  emits 'player_ready'
#   Server:  updates its state, then emits 'lobby_state' to the whole room
#   All clients: re-render their screens based on what they were told
#
# Each function below is registered as a handler for one event name
# using the @socketio.on(...) decorator. Flask-SocketIO calls the
# matching function automatically whenever a client emits that event —
# you never have to write your own "which event was this?" dispatch
# code (unlike the raw `ws` library in Node, where we built that by hand)

#if you get an error here make sure to download socketio and flask_socketio using pip install socketio flask_socketio
from flask_socketio import emit, join_room
from app.extensions import socketio
from app.sockets.sessions import get_or_create_session, get_session, sessions, change_host
import time
from app.services.scoring_service import build_result_state


@socketio.on('join_session')
def handle_join_session(payload):
    """
    payload example: { "sessionCode": "ABCD", "name": "Bernadette", "playerId": null }

    Runs once, right when a player first opens the lobby page and
    connects. `request.sid` (imported below) is Flask-SocketIO's way of
    identifying THIS specific browser tab's connection — think of it as
    the Python equivalent of the raw `socket` object we stored per
    player in the Node version.
    """
    from flask import request  # local import keeps this file's top imports focused

    session_code = payload['sessionCode']
    is_host = payload.get('isHost', False)

    # Hosts create a session, joining players must use an existing session
    if is_host:
        session = get_or_create_session(session_code)
    else:
        session = get_session(session_code)

        if session is None:
            emit('invalid_session')
            return

    # RECONNECT SUPPORT: if the client already has a playerId saved from
    # before (e.g. their WiFi dropped and the page reconnected), reuse
    # their old player record instead of creating a brand new one.
    player_id = payload.get('playerId')
    if player_id and player_id in session['players']:
        player = session['players'][player_id]
        player['connected'] = True
        player['socket_id'] = request.sid
    else:
        import uuid
        player_id = str(uuid.uuid4())  # unique so we never mix up two different players
        player = {
            'name': payload.get('name') or f"Player {len(session['players']) + 1}",
            'ready': False,
            'connected': True,
            'socket_id': request.sid,
        }
        session['players'][player_id] = player
        
    # If this player created the game, remember them as the host
    if is_host and session['host_id'] is None:
        session['host_id'] = player_id

    # JOIN_ROOM is Flask-SocketIO's version of "put this connection in
    # the group of sockets that belong to session ABCD". Once a
    # connection is in a room, `emit(..., room='ABCD')` will reach it
    # automatically — we never manually loop over connections ourselves.
    join_room(session_code)

    # Tell THIS player (and only this player) their assigned ID, so
    # their browser can save it and send it back if they reconnect later.
    # `emit` with no `room` argument sends only to whoever triggered
    # this handler — the equivalent of `socket.send(...)` in the Node version.
    joined_data = {
        'playerId': player_id,
        'phase': session['phase'],
        'isHost': player_id == session['host_id']
}

    # If the auction has already started, tell this player when it started
    # so their timer can match everyone else's timer
    if session['phase'] == 'auction' and 'auction_start_time' in session:
        joined_data['auctionStartTime'] = session['auction_start_time']

    emit('joined', joined_data)

    broadcast_lobby_state(session_code, session)
    if session.get('auction') and session['phase'] in ('auction', 'mission'):
        from app.sockets.handlers.auction import emit_auction_state_to_player
        emit_auction_state_to_player(session, player_id)
    if session.get('mission') and session['phase'] == 'mission':
        from app.sockets.handlers.mission import emit_mission_state_to_player
        emit_mission_state_to_player(session)
        
    # send stored results for when a player arrives or reconnects.
    if session['phase'] == 'result_page':
        result_state = build_result_state(session)

        if result_state is None:
            emit('result_error', {
                'message': 'Results are not available for this game yet.'
            })
        else:
            emit('result_state', result_state)

def reassign_host_after_disconnect(session_code, old_host_id):
    """
    Wait 30 seconds after the host disconnects.
    If they have not reconnected, give host to another connected player.
    """
    socketio.sleep(30)

    session = get_session(session_code)

    # Session may no longer exist
    if session is None:
        return

    # Make sure this player is still the host
    if session["host_id"] != old_host_id:
        return

    old_host = session["players"].get(old_host_id)

    # Host rejoined during the 30 seconds
    if old_host and old_host["connected"]:
        return

    new_host_id = change_host(session)

    if new_host_id:
        socketio.emit(
            'host_changed',
            {'hostId': new_host_id},
            room=session_code
    )

    broadcast_lobby_state(session_code, session)

@socketio.on('disconnect')
def handle_disconnect():
    from flask import request

    # Find which player belonged to this socket
    for session_code, session in sessions.items():
        for player_id, player in session['players'].items():

            if player.get('socket_id') == request.sid:
                player['connected'] = False
                player['socket_id'] = None

                broadcast_lobby_state(session_code, session)

                # If the host disconnected, give them 30 seconds to reconnect
                # before transferring host to another connected player.
                if player_id == session['host_id']:
                    socketio.start_background_task(
                        reassign_host_after_disconnect,
                        session_code,
                        player_id
                    )

                return


@socketio.on('player_ready')
def handle_player_ready(payload):
    """
    payload example: { "playerId": "...", "ready": true }

    NOTE: we need the client to tell us their playerId in the payload, 
    since Flask-SocketIO's `request.sid`changes on every reconnect. 
    Make sure your frontend always includes the playerId it got back 
    from the 'joined' event in future messages that need to know who sent them.
    """
    session_code = payload['sessionCode']
    session = get_or_create_session(session_code)
    player = session['players'].get(payload['playerId'])
    if not player:
        return  # unknown player — ignore rather than crash

    player['ready'] = bool(payload.get('ready'))
    broadcast_lobby_state(session_code, session)

    # PHASE TRANSITION:
    # Once every player has readied up and there are enough players,
    # the host can move the game forward.
    # Copy this "check a condition across all players, then change phase
    # and broadcast it" pattern in auction.py/mission.py.
@socketio.on('start_game')
def handle_start_game(payload):
    session_code = payload['sessionCode']
    session = get_or_create_session(session_code)

    # Make sure only the host can start the game
    if payload['playerId'] != session['host_id']:
        return

    all_ready = all(p['ready'] for p in session['players'].values())

    # The lobby permits the host to start with however many players are
    # currently in the room, provided everyone has marked themselves ready
    if all_ready and session['players']:
        # Initialise shared auction state before players navigate away.
        from app.sockets.handlers.auction import initialise_auction
        initialise_auction(session)
        session['phase'] = 'start_game'
        emit('game_started', {'phase': session['phase']}, room=session_code)

        # TODO (auction teammate): initialise session['auction'] = {...}
        # here, then call a broadcast_auction_state(session_code, session)
        # function (mirroring broadcast_lobby_state below) so clients get
        # the first auction screen's data.

@socketio.on('start_auction')
def handle_start_auction(payload):
    session_code = payload['sessionCode']
    session = get_session(session_code)

    # Session must exist
    if session is None:
        return

    # Only the host can start the auction
    if payload['playerId'] != session['host_id']:
        return

    # Only move forward from the start game phase
    if session['phase'] != 'start_game':
        return

    # Update the session's current phase
    session['phase'] = 'auction'

    # Remember when the auction started so rejoining players
    # continue from the same timer instead of restarting it
    session['auction_start_time'] = time.time()

    # Tell everyone in the session to move to the auction
    emit('auction_started', {
    'phase': session['phase'],
    'auctionStartTime': session['auction_start_time']
}, room=session_code)

def broadcast_lobby_state(session_code, session):
    """
    Sends the current player list + phase to EVERYONE in this session's
    room. Follow this exact pattern for auction/mission — a small
    "build the payload, then emit it to the room" function per phase.
    """
    players = [
        {'id': pid, 'name': p['name'], 'ready': p['ready'], 'connected': p['connected'],'isHost': pid == session['host_id']}
        for pid, p in session['players'].items()
    ]
    socketio.emit(
    'lobby_state',
    {'players': players, 'phase': session['phase']},
    room=session_code
    )
