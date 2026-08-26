# =====================================================================
# HANDLERS/AUCTION.PY — logic for the auction phase (TODO)
# =====================================================================
#
# Follow the exact pattern worked through in handlers/lobby.py:
#   1. @socketio.on('event_name') registers a function for one message type
#   2. Read/update session state (imported via get_or_create_session)
#   3. emit(...) the new state to everyone in the room: room=session_code
#
# SUGGESTED SHAPE for the auction slice of session state (add this
# where lobby.py currently says "TODO: initialise session['auction']"):
#
#   session['auction'] = {
#       'current_item_pair': None,   # the two items currently up for bid
#       'bids': {},                  # playerId -> bid amount
#       'current_challenge_index': 0,
#   }

# This file just needs to be imported somewhere (see handlers/__init__.py)
# for its @socketio.on(...) decorators to take effect once you add them
