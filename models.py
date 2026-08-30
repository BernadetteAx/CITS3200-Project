"""
models.py

PURPOSE:
    Defines the database models for the Chaos Auction game
    using SQLAlchemy.

    Models represent the data that needs to be stored, such as:
    - Games
    - Players
    - Items
    - Missions
    - Challenges
    - Votes
    - Results/outcomes

    This file defines WHAT data exists.

    Game rules and Socket.IO events should NOT be placed here.
"""

from .extensions import db


# ============================================================
# GAME
# ============================================================

class Game(db.Model):
    """
    Represents one game/session.

    Example:
        session_code = "ABC123"
        state = "LOBBY"
        team_money = 1000
    """

    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)

    # Unique code that players enter to join this game.
    session_code = db.Column(
        db.String(10),
        unique=True,
        nullable=False
    )

    # Current stage of the game.
    # Example values:
    # "LOBBY", "AUCTION", "MISSION", "RESULT"
    state = db.Column(
        db.String(30),
        nullable=False,
        default="LOBBY"
    )

    # ID of the player currently acting as host.
    host_player_id = db.Column(
        db.Integer,
        nullable=True
    )

    # Team's current money.
    team_money = db.Column(
        db.Integer,
        nullable=False,
        default=1000
    )

    # Current mission/challenge position.
    current_mission_id = db.Column(
        db.String(50),
        nullable=True
    )

    current_challenge_index = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )


# ============================================================
# PLAYER
# ============================================================

class Player(db.Model):
    """
    Represents one player inside a game.

    Players do not need an account.
    """

    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)

    game_id = db.Column(
        db.Integer,
        db.ForeignKey("games.id"),
        nullable=False
    )

    # Randomly generated name, which the player can change.
    name = db.Column(
        db.String(50),
        nullable=False
    )

    # Used to determine who joined first, including possible
    # host-transfer behaviour.
    join_order = db.Column(
        db.Integer,
        nullable=False
    )

    # Whether the player is currently connected.
    connected = db.Column(
        db.Boolean,
        default=True
    )


# ============================================================
# ITEM
# ============================================================

class Item(db.Model):
    """
    Represents an item that can be purchased/owned/used.

    The exact item fields should be adjusted to the agreed
    game requirements.
    """

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    price = db.Column(
        db.Integer,
        nullable=False
    )


# ============================================================
# MISSION
# ============================================================

class Mission(db.Model):
    """
    Represents a mission available in the game.

    A mission contains multiple challenges.

    Example:

        Mission: The Heist
            Challenge 1
            Challenge 2
            Challenge 3
    """

    __tablename__ = "missions"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )


# ============================================================
# CHALLENGE
# ============================================================

class Challenge(db.Model):
    """
    Represents one challenge within a mission.

    Challenges should be ordered so the server knows
    which challenge comes next.
    """

    __tablename__ = "challenges"

    id = db.Column(db.Integer, primary_key=True)

    mission_id = db.Column(
        db.Integer,
        db.ForeignKey("missions.id"),
        nullable=False
    )

    # Position within the mission.
    challenge_index = db.Column(
        db.Integer,
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    # Item that can potentially solve this challenge.
    # Exact implementation may change depending on the
    # final game design.
    required_item_id = db.Column(
        db.Integer,
        nullable=True
    )


# ============================================================
# VOTE
# ============================================================

class Vote(db.Model):
    """
    Represents a player's vote during an auction or mission.

    The server should ensure that a player cannot have
    multiple active votes for the same voting round.
    """

    __tablename__ = "votes"

    id = db.Column(db.Integer, primary_key=True)

    game_id = db.Column(
        db.Integer,
        db.ForeignKey("games.id"),
        nullable=False
    )

    player_id = db.Column(
        db.Integer,
        db.ForeignKey("players.id"),
        nullable=False
    )

    # "AUCTION" or "MISSION"
    vote_type = db.Column(
        db.String(30),
        nullable=False
    )

    # ID of the selected item/choice.
    choice_id = db.Column(
        db.String(100),
        nullable=False
    )


# ============================================================
# TODO
# ============================================================

# Add additional models when the exact requirements are agreed.
#
# Possible future models:
#
# - InventoryItem
# - Auction
# - AuctionOutcome
# - MissionOutcome
# - ChallengeOutcome
# - Score
#
# Avoid creating unnecessary tables until the team's
# actual requirements have been confirmed.
