# =====================================================================
# HANDLERS/MISSION.PY — logic for the mission phase (TO BE BUILT)
# =====================================================================
#
# Same pattern again — see handlers/lobby.py for the fully worked example
#
# SUGGESTED SHAPE for the mission slice of session state:
#
#   session['mission'] = {
#       'challenges': [...],          # sequence of challenges for this mission
#       'current_challenge_index': 0,
#       'log': [],                    # history of resolved challenges
#   }

# This file just needs to be imported somewhere (see handlers/__init__.py)
# for its @socketio.on(...) decorators to take effect once you add them.