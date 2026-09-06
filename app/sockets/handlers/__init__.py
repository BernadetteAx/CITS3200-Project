# =====================================================================
# HANDLERS/__init__.py — makes sure every handler file's @socketio.on
# decorators actually run
# =====================================================================
#
# In Python, decorators like @socketio.on('player_ready') only take
# effect once the file containing them has been IMPORTED somewhere —
# just having the file exist isn't enough, Python has to actually read
# and run it once
#
# This file's only job is to import lobby.py, auction.py, and
# mission.py so that whatever imports app.sockets.handlers causes all 
# three to be loaded, and all their event handlers to get registered with socketio
#
# You will NOT need to edit this file you only touch it if you 
# ever add a whole NEW phase file (lobby, auction, mission, ........)

from app.sockets.handlers import lobby
from app.sockets.handlers import auction
from app.sockets.handlers import mission
