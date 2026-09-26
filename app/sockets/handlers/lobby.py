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

# if you get an error here make sure to download socketio and flask_socketio
# using pip install socketio flask_socketio
from flask_socketio import emit, join_room, leave_room
from app.extensions import socketio
from app.sockets.sessions import (
    get_or_create_session,
    get_session,
    sessions,
    change_host,
)
import time
from app.services.scoring_service import build_result_state


@socketio.on('join_session')
def handle_join_session(payload):
    """
    payload example:
    { "sessionCode": "ABCD", "name": "Bernadette", "playerId": null }

    Runs once, right when a player first opens the lobby page and
    connects. `request.sid` is Flask-SocketIO's way of identifying
    this specific browser tab's connection.
    """
    from flask import request

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

    # RECONNECT SUPPORT
    player_id = payload.get('playerId')

    if player_id and player_id in session['players']:
        player = session['players'][player_id]
        player['connected'] = True
        player['socket_id'] = request.sid
    else:
        import uuid

        player_id = str(uuid.uuid4())
        player = {
            'name': payload.get('name')
            or f"Player {len(session['players']) + 1}",
            'ready': False,
            'connected': True,
            'socket_id': request.sid,
        }
        session['players'][player_id] = player

    # If this player created the game, remember them as the host
    if is_host and session['host_id'] is None:
        session['host_id'] = player_id

    join_room(session_code)

    joined_data = {
        'playerId': player_id,
        'phase': session['phase'],
        'isHost': player_id == session['host_id'],
    }

    # If the auction has already started, tell this player when it started
    if session['phase'] == 'auction' and 'auction_start_time' in session:
        joined_data['auctionStartTime'] = session['auction_start_time']

    emit('joined', joined_data)

    broadcast_lobby_state(session_code, session)

    if session.get('auction') and session['phase'] in ('auction', 'mission'):
        from app.sockets.handlers.auction import emit_auction_state_to_player
        emit_auction_state_to_player(session, player_id)

    if session.get('mission') and session['phase'] == 'mission':
        from app.sockets.handlers.mission import emit_mission_state_to_player
        emit_mission_state_to_player(session, player_id)

    # Send stored results when a player arrives or reconnects
    if session['phase'] == 'result_page':
        result_state = build_result_state(session)

        if result_state is None:
            emit(
                'result_error',
                {'message': 'Results are not available for this game yet.'},
            )
        else:
            emit('result_state', result_state)


def reassign_host_after_disconnect(session_code, old_host_id):
    """
    Wait 30 seconds after the host disconnects.
    If they have not reconnected, give host to another connected player.
    """
    socketio.sleep(30)

    session = get_session(session_code)

    if session is None:
        return

    if session['host_id'] != old_host_id:
        return

    old_host = session['players'].get(old_host_id)

    # Host rejoined during the 30 seconds
    if old_host and old_host['connected']:
        return

    new_host_id = change_host(session)

    if new_host_id:
        socketio.emit(
            'host_changed',
            {'hostId': new_host_id},
            room=session_code,
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

                # A disconnected player must not block auction voting.
                # Keep the player in the session so they can reconnect.
                if (
                    session.get('phase') == 'auction'
                    and session.get('auction')
                ):
                    from app.sockets.handlers.auction import (
                        handle_player_disconnected,
                    )
                    handle_player_disconnected(session_code, session)

                if session.get('phase') == 'mission' and session.get('mission'):
                    from app.sockets.handlers.mission import handle_player_disconnected
                    handle_player_disconnected(session_code, session)

                # Give a disconnected host 30 seconds to reconnect.
                if player_id == session['host_id']:
                    socketio.start_background_task(
                        reassign_host_after_disconnect,
                        session_code,
                        player_id,
                    )

                return


@socketio.on('leave_session')
def handle_leave_session(payload):
    """Permanently remove a player who deliberately leaves a game."""
    from flask import request

    if not isinstance(payload, dict):
        return {'ok': False}

    session_code = payload.get('sessionCode')
    player_id = payload.get('playerId')
    session = get_session(session_code)

    if not session or not player_id:
        return {'ok': False}

    # Only allow the socket belonging to this player to remove them.
    player = session['players'].get(player_id)

    if not player or player.get('socket_id') != request.sid:
        return {'ok': False}

    was_host = player_id == session.get('host_id')

    del session['players'][player_id]
    leave_room(session_code)

    # If voting is underway, immediately re-evaluate using the
    # players who remain in the game.
    if session.get('phase') == 'auction' and session.get('auction'):
        from app.sockets.handlers.auction import handle_player_left
        handle_player_left(session_code, session, player_id)

    if session.get('phase') == 'mission' and session.get('mission'):
        from app.sockets.handlers.mission import handle_player_left
        handle_player_left(session_code, session, player_id)

    if was_host:
        session['host_id'] = None
        new_host_id = change_host(session)

        if new_host_id:
            socketio.emit(
                'host_changed',
                {'hostId': new_host_id},
                room=session_code,
            )

    # Delete an empty session; otherwise update remaining players.
    if not session['players']:
        del sessions[session_code]
    else:
        broadcast_lobby_state(session_code, session)

    emit('left_session')
    return {'ok': True}


@socketio.on('play_again')
def handle_play_again(payload):
    session_code = payload.get('sessionCode')
    session = get_session(session_code)

    if (
        session is None
        or session.get('phase') != 'result_page'
        or payload.get('playerId') != session.get('host_id')
    ):
        return

    session['phase'] = 'lobby'

    for player in session['players'].values():
        player['ready'] = False

    for key in (
        'generated_mission',
        'auction',
        'auction_start_time',
        'purchased_items',
        'mission',
        'mission_result',
    ):
        session.pop(key, None)

    socketio.emit('play_again_started', room=session_code)
    broadcast_lobby_state(session_code, session)


@socketio.on('player_ready')
def handle_player_ready(payload):
    """
    payload example: { "playerId": "...", "ready": true }
    """
    session_code = payload['sessionCode']
    session = get_or_create_session(session_code)
    player = session['players'].get(payload['playerId'])

    if not player:
        return

    player['ready'] = bool(payload.get('ready'))
    broadcast_lobby_state(session_code, session)


@socketio.on('start_game')
def handle_start_game(payload):
    session_code = payload['sessionCode']
    session = get_or_create_session(session_code)

    # Make sure only the host can start the game
    if payload['playerId'] != session['host_id']:
        return

    all_ready = all(
        player['ready']
        for player in session['players'].values()
    )

    # Start when everyone currently in the room is ready
    if all_ready and session['players']:
        session['phase'] = 'start_game'
        emit(
            'game_started',
            {'phase': session['phase']},
            room=session_code,
        )


@socketio.on('start_auction')
def handle_start_auction(payload):
    session_code = payload['sessionCode']
    session = get_session(session_code)

    if session is None:
        return

    # Only the host can start the auction
    if payload['playerId'] != session['host_id']:
        return

    # Only move forward from the start game phase
    if session['phase'] != 'start_game':
        return

    session['phase'] = 'auction'

    # Remember when the auction started so rejoining players
    # continue from the same timer instead of restarting it.
    session['auction_start_time'] = time.time()

    emit(
        'auction_started',
        {
            'phase': session['phase'],
            'auctionStartTime': session['auction_start_time'],
        },
        room=session_code,
    )


def broadcast_lobby_state(session_code, session):
    """Send the current public lobby state to everyone in the session."""
    players = [
        {
            'id': player_id,
            'name': player['name'],
            'ready': player['ready'],
            'connected': player['connected'],
            'isHost': player_id == session['host_id'],
        }
        for player_id, player in session['players'].items()
    ]

    socketio.emit(
        'lobby_state',
        {
            'players': players,
            'phase': session['phase'],
        },
        room=session_code,
    )
