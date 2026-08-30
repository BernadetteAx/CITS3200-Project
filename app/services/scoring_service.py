"""
scoring_service.py

PURPOSE:
    Handles score calculation.

    This keeps scoring rules separate from:
    - Mission Socket.IO events
    - Auction Socket.IO events
    - Frontend JavaScript

    IMPORTANT:
    Exact successful/failed challenge scores should only be
    implemented once confirmed by the Client/team.
"""


def apply_challenge_success(game):
    """
    Apply the agreed score for a successful challenge.

    TODO:
        Use the final Client-approved score.
    """
    pass


def apply_challenge_failure(game):
    """
    Apply the agreed penalty for a failed challenge.

    TODO:
        Use the final Client-approved penalty.
    """
    pass


def get_final_score(game):
    """
    Return the team's final score.
    """
    pass
