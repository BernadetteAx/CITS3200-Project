# =====================================================================
# SOCKETS/__init__.py — registers all socket event handlers
# =====================================================================
#
# Importing app.sockets.handlers (see that folder's __init__.py) causes
# lobby.py/auction.py/mission.py to be imported in turn, which is what
# actually registers their @socketio.on(...) event handlers. This file
# exists so that app/__init__.py only needs one line
# ("from app import sockets") to pull in the whole system, without
# needing to know about the handlers/ subfolder specifically

from app.sockets import handlers
