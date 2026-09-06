from flask import Flask, render_template
from app.extensions import socketio

app = Flask(__name__)

# Connect SocketIO to Flask
socketio.init_app(app)

# Load normal routes
from app import routes

# Load WebSocket handlers
from app import sockets