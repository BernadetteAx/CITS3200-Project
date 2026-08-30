"""
config.py

PURPOSE:
    Stores configuration/settings for the Flask application.

    Keep settings such as:
    - Secret key
    - Database location
    - Flask-SocketIO settings
    - Testing/development settings

    Other files should import configuration from here instead
    of hard-coding these values throughout the project.
"""

import os


class Config:
    # Secret key used by Flask sessions/security features.
    # For the final project, this should ideally come from an
    # environment variable rather than being committed as a real secret.
    SECRET_KEY = os.environ.get("SECRET_KEY", "development-secret-key")

    # SQLite database used to store game information.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///chaos_auction.db"
    )

    # Disable SQLAlchemy's event system unless specifically needed.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-SocketIO configuration.
    # Adjust if the project later requires a different setting.
    SOCKETIO_ASYNC_MODE = "threading"
