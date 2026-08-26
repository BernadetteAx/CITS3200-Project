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
from app.sockets.sessions import get_or_create_session


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
    session = get_or_create_session(session_code)

    # RECONNECT SUPPORT: if the client already has a playerId saved from
    # before (e.g. their WiFi dropped and the page reconnected), reuse
    # their old player record instead of creating a brand new one.
    player_id = payload.get('playerId')
    if player_id and player_id in session['players']:
        player = session['players'][player_id]
        player['connected'] = True
    else:
        import uuid
        player_id = str(uuid.uuid4())  # unique so we never mix up two different players
        player = {
            'name': payload.get('name') or f"Player {len(session['players']) + 1}",
            'ready': False,
            'connected': True,
        }
        session['players'][player_id] = player

    # JOIN_ROOM is Flask-SocketIO's version of "put this connection in
    # the group of sockets that belong to session ABCD". Once a
    # connection is in a room, `emit(..., room='ABCD')` will reach it
    # automatically — we never manually loop over connections ourselves.
    join_room(session_code)

    # Tell THIS player (and only this player) their assigned ID, so
    # their browser can save it and send it back if they reconnect later.
    # `emit` with no `room` argument sends only to whoever triggered
    # this handler — the equivalent of `socket.send(...)` in the Node version.
    emit('joined', {'playerId': player_id})

    broadcast_lobby_state(session_code, session)


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

    # PHASE TRANSITION example: once every player has readied up (and
    # there are enough players), move the game forward. Copy this
    # "check a condition across all players, then change phase and
    # broadcast it" pattern in auction.py/mission.py.
    all_ready = all(p['ready'] for p in session['players'].values())
    if all_ready and len(session['players']) >= 3:
        session['phase'] = 'auction'
        emit('game_started', {'phase': session['phase']}, room=session_code)
        # TODO (auction teammate): initialise session['auction'] = {...}
        # here, then call a broadcast_auction_state(session_code, session)
        # function (mirroring broadcast_lobby_state below) so clients get
        # the first auction screen's data.


def broadcast_lobby_state(session_code, session):
    """
    Sends the current player list + phase to EVERYONE in this session's
    room. Follow this exact pattern for auction/mission — a small
    "build the payload, then emit it to the room" function per phase.
    """
    players = [
        {'id': pid, 'name': p['name'], 'ready': p['ready'], 'connected': p['connected']}
        for pid, p in session['players'].items()
    ]
    emit('lobby_state', {'players': players, 'phase': session['phase']}, room=session_code)
