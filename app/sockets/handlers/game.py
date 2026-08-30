"""
game.py

PURPOSE:
    Handles general game-state Socket.IO events.

    Use this file for events that affect the overall game,
    rather than a specific Auction or Mission.

    Examples:
    - Starting the game
    - Changing game phase
    - Sending current game state
    - General game synchronisation
"""

from flask_socketio import emit


# TODO:
# @socketio.on("start_game")
# def handle_start_game(data):
#     ...


# TODO:
# Send the current game state to a newly connected/reconnected
# player when appropriate.
#
# @socketio.on("request_game_state")
# def handle_request_game_state():
#     ...
