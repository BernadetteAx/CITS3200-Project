# =====================================================================
# EXTENSIONS.PY — holds the shared SocketIO instance
# =====================================================================
#
# WHY THIS FILE EXISTS (a common Flask gotcha):
# Every file that defines a `@socketio.on(...)` handler needs access to
# the same `socketio` object that your Flask app is using. But if we
# created `socketio` directly inside app/__init__.py and then tried to
# import it from there into app/sockets/handlers/lobby.py, and
# app/__init__.py ALSO needs to import those handler files (to register
# them) — we'd get a "circular import" error, where two files are each
# trying to load the other before either has finished loading.
#
# The fix: put the plain, un-initialised SocketIO() object in its own
# tiny file with no other dependencies. Every other file (handlers,
# app/__init__.py) imports it FROM HERE, so there's only one direction
# of importing, never a loop.

from flask_socketio import SocketIO

socketio = SocketIO()
