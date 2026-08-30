"""
game_service.py

PURPOSE:
    Contains the core game/session logic.

    This file handles operations such as:
    - Creating a game
    - Joining a game
    - Removing a player
    - Changing the host
    - Starting the game
    - Changing game phases
    - Getting the current game state

    This file should NOT contain Socket.IO event decorators.
    Socket.IO handlers should call these functions instead.
"""

from ..models import Game, Player
from ..extensions import db


def create_game():
    """
    Create and return a new game.

    TODO:
        - Generate a unique session code.
        - Create Game record.
        - Set initial state to LOBBY.
        - Set team money to $1000.
        - Save to database.
    """
    pass


def join_game(session_code, player_name):
    """
    Add a player to an existing game.

    TODO:
        - Find game using session_code.
        - Validate that the game can be joined.
        - Create Player.
        - Assign join order.
        - Save player.
        - Return game/player.
    """
    pass


def remove_player(player_id):
    """
    Remove/disconnect a player from a game.

    TODO:
        - Mark player as disconnected.
        - Do not automatically stop an active game.
        - Handle host leaving if necessary.
    """
    pass


def transfer_host(game):
    """
    Transfer hosting responsibility to another player.

    TODO:
        - Find appropriate replacement player.
        - User stories suggest the player who joined first.
        - Update game.host_player_id.
    """
    pass


def start_game(game, player):
    """
    Start the game.

    TODO:
        - Verify player is the host.
        - Verify game is in a valid state.
        - Select a mission.
        - Prepare challenge sequence.
        - Change game state to the first gameplay phase.
    """
    pass


def change_phase(game, new_state):
    """
    Change the current game phase.

    Example:
        LOBBY -> AUCTION
        AUCTION -> MISSION
        MISSION -> AUCTION
        MISSION -> RESULT
    """
    pass


def get_game_state(game):
    """
    Return the information clients need to display
    the current game state.

    TODO:
        Return a safe dictionary containing information
        that should be sent to connected players.
    """
    pass
