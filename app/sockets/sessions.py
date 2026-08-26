# =====================================================================
# SESSIONS.PY — where all active games are stored while the server runs
# =====================================================================
#
# A "session" = one instance of the game being played by one group of
# friends, identified by their join code (e.g. "ABCD")
#
# NOTE ON FLASK-SOCKETIO "ROOMS":
# We only need to track game DATA (player names, ready status, phase), not
# connection objects, compared to using Nodes 'ws' library
#
# IMPORTANT LIMITATION: this all lives in server memory (a plain Python
# dict). If the server restarts, every session disappears. Fine for a
# uni project, unless we wanna go the extra mile we can add a database later

sessions = {}
# Shape of one entry once created:
# sessions["ABCD"] = {
#     "phase": "lobby",              # which part of the game we're in
#     "host_id": None,               # player ID of the person hosting
#     "players": {
#         "player-id-1": {"name": "...", "ready": False, "connected": True},
#         ...
#     },
#     # "auction": {...}   <- added once auction.py initialises it
#     # "mission": {...}   <- added once mission.py initialises it
# }


def get_or_create_session(session_code):
    """
    Look up a session by its join code, creating it if this is the
    first player to use that code. This means the FIRST player to
    enter a code effectively creates the game session for everyone
    else who joins afterwards — no separate "create game" step needed
    """
    if session_code not in sessions:
        sessions[session_code] = {
            "phase": "lobby",
            "host_id": None,
            "players": {},
        }
    return sessions[session_code]
