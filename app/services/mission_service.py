"""
mission_service.py

PURPOSE:
    Contains the rules and data handling for missions.

    A mission contains multiple challenges.

    Example:

        The Heist
        ├── Challenge 1
        ├── Challenge 2
        ├── Challenge 3
        └── Challenge 4

    This file determines:
    - Which mission is active.
    - Which challenge is currently active.
    - Which items can be used.
    - How mission votes are resolved.
    - Whether a challenge succeeds/fails.
    - Which items are consumed.
    - When to move to the next challenge.

    Socket.IO communication belongs in:
        sockets/handlers/mission.py
"""

def get_current_challenge(game):
    """
    Return the challenge currently being played.

    TODO:
        - Find the game's current mission.
        - Read game.current_challenge_index.
        - Return the corresponding challenge.
    """
    pass


def get_usable_items(game, challenge):
    """
    Return team-owned items that are available for
    the current challenge.

    TODO:
        - Check team inventory.
        - Remove already-used items.
        - Determine which items can help with challenge.
    """
    pass


def validate_vote(game, player, choice_id):
    """
    Validate a player's mission vote.

    Reject:
        - Player not in game.
        - Invalid choice.
        - Vote after voting has ended.
        - Invalid game state.
    """
    pass


def resolve_mission_vote(game):
    """
    Resolve the mission vote after the voting period ends.

    TODO:
        - Count votes.
        - Handle ties.
        - Determine whether an item is selected.
        - Determine success/failure.
        - Consume item if used.
        - Record challenge outcome.
    """
    pass


def record_challenge_outcome(game, challenge, success):
    """
    Record whether the challenge succeeded or failed.

    TODO:
        - Store outcome for Result page.
        - Apply score change/penalty once confirmed.
    """
    pass


def advance_challenge(game):
    """
    Move the game to the next challenge.

    TODO:
        - Increase current_challenge_index.
        - Check whether another challenge exists.
        - If another challenge exists, return it.
        - If no challenges remain, transition toward Result.
    """
    pass
