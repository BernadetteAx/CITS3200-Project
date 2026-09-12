"""Authoritative Socket.IO state and actions for the mission phase."""

import random
import re

from flask import request
from flask_socketio import emit

from app.extensions import socketio
from app.game_data.challenges import challenges_dict
from app.game_data.mission_structs import missions_list
from app.sockets.sessions import get_session


possible_locations = [
    "Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano",
]

ITEM_NAME_TO_ID = {
    "Fire Starter Kit": "fuel",
    "Handheld Radios": "gps",
    "Mirror": "credit-card",
    "Gas Mask and Knockout Gas": "armor",
    "Ice Axes": "axe",
    "Armoured Truck": "car",
    "Rope": "mountain-gear",
    "Paraglider": "mountain-gear",
    "Helicopter": "car",
    "Grapling Hook": "toolkit",
    "Scuba Gear": "mountain-gear",
    "Wire Cutters": "toolkit",
    "Explosives": "toolkit",
    "Water Bottle": "water-bottle",
}


def _item_ids(item_names):
    """Translate submitted item names to auction inventory IDs."""
    return [
        ITEM_NAME_TO_ID[item_name]
        for item_name in item_names
        if item_name in ITEM_NAME_TO_ID
    ]


def _challenge_id(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def generate_mission():
    """Generate a mission from the submitted game data."""
    location = random.choice(possible_locations)
    mission_options = [
        mission
        for mission in missions_list
        if location in mission["location_options"]
    ]
    mission = random.choice(mission_options)
    mission_type = mission["mission_type"]
    challenges = []

    for challenge_number in range(1, 7):
        challenge_type = mission[f"challenge_{challenge_number}"]
        challenge_options = [
            challenge
            for challenge in challenges_dict[challenge_type].values()
            if location in challenge["viable_locations"]
            and mission_type in challenge["viable_mission_types"]
        ]
        if not challenge_options:
            raise ValueError(
                f"No {challenge_type} challenge is valid for "
                f"{mission['mission_name']} in {location}"
            )

        challenge = random.choice(challenge_options)
        challenges.append({
            "id": _challenge_id(challenge["challenge_name"]),
            "name": challenge["challenge_name"],
            "type": challenge_type,
            "location": location,
            "description": challenge["desc"] or (
                f"Your team encounters: {challenge['challenge_name']}."
            ),
            "success_items": _item_ids(challenge.get("items", {}).keys()),
        })

    return {
        "location": location,
        "name": mission["mission_name"],
        "type": "Rescue Op" if mission_type == "Rescue" else mission_type,
        "challenges": challenges,
    }


def initialise_mission(session):
    """Create mission state once, retaining the auction's team inventory."""
    if not session.get("mission"):
        generated = generate_mission()

        session["mission"] = {
            "name": generated["name"],
            "type": generated["type"],
            "location": generated["location"],
            "challenges": generated["challenges"],
            "current_challenge_index": 0,
            "inventory": [
                dict(item)
                for item in session.get("purchased_items", [])
            ],
            "used_items": [],
            "outcome_log": [],
            "score": 100,
            "penalties": 0,
            "status": "active",
            "outcome": None,
        }

    return session["mission"]


def _valid_player(session, payload):
    if not isinstance(payload, dict) or not payload.get("sessionCode"):
        return None
    player_id = payload.get("playerId")
    player = session["players"].get(player_id)
    if not player or player.get("socket_id") != request.sid:
        return None
    return player_id


def _state(session):
    mission = session["mission"]
    index = mission["current_challenge_index"]
    current = mission["challenges"][index] if index < len(mission["challenges"]) else None
    used = set(mission["used_items"])
    inventory = [
        {**item, "used": item["id"] in used}
        for item in mission["inventory"]
    ]
    return {
        "phase": session["phase"],
        "missionName": mission["name"],
        "missionType": mission["type"],
        "location": mission["location"],
        "currentChallengeIndex": index,
        "totalChallenges": len(mission["challenges"]),
        "challenge": current,
        "inventory": inventory,
        "usedItems": list(mission["used_items"]),
        "outcomeLog": list(mission["outcome_log"]),
        "score": mission["score"],
        "penalties": mission["penalties"],
        "status": mission["status"],
        "outcome": mission["outcome"],
    }


def broadcast_mission_state(session_code, session):
    socketio.emit("mission_state", _state(session), room=session_code)


def emit_mission_state_to_player(session):
    if session.get("mission"):
        emit("mission_state", _state(session))


def _action_session(payload):
    code = payload.get("sessionCode") if isinstance(payload, dict) else None
    session = get_session(code)
    if not session or session.get("phase") != "mission" or not session.get("mission"):
        return None, None, None
    player = _valid_player(session, payload)
    mission = session["mission"]
    if not player or payload.get("challengeIndex") != mission["current_challenge_index"]:
        return None, None, None
    return code, session, mission


def _resolve(code, session, mission, item=None):
    challenge = mission["challenges"][mission["current_challenge_index"]]
    if item:
        mission["used_items"].append(item["id"])
        successful = item["id"] in challenge["success_items"]
        title = "Obstacle Cleared" if successful else "A Costly Detour"
        description = (
            f"The {item['name']} gets the team past the challenge."
            if successful
            else f"The {item['name']} was not enough; the team takes a longer route."
        )
    else:
        successful = False
        title = "Forced to Double Back"
        description = "No item was used, so the team took the longer route."

    penalty = 0 if successful else 10
    mission["penalties"] += penalty
    mission["score"] = max(0, mission["score"] - penalty)
    outcome = {
        "challengeId": challenge["id"],
        "challengeIndex": mission["current_challenge_index"],
        "item": item,
        "success": successful,
        "penalty": penalty,
        "title": title,
        "description": description,
    }
    mission["outcome"] = outcome
    mission["outcome_log"].append(outcome)
    mission["status"] = "resolved"
    broadcast_mission_state(code, session)
    socketio.emit("mission_outcome", outcome, room=code)


@socketio.on("mission_use_item")
def mission_use_item(payload):
    code, session, mission = _action_session(payload)
    if not session or mission["status"] != "active":
        return
    item_id = payload.get("itemId")
    item = next(
        (item for item in mission["inventory"] if item["id"] == item_id),
        None,
    )
    if not item or item_id in mission["used_items"]:
        return
    _resolve(code, session, mission, item)


@socketio.on("mission_continue")
def mission_continue(payload):
    code, session, mission = _action_session(payload)
    if session and mission["status"] == "active":
        _resolve(code, session, mission)


@socketio.on("mission_advance")
def mission_advance(payload):
    code, session, mission = _action_session(payload)
    if not session or mission["status"] != "resolved":
        return
    mission["current_challenge_index"] += 1
    mission["outcome"] = None
    if mission["current_challenge_index"] >= len(mission["challenges"]):
        mission["status"] = "complete"
        session["mission_result"] = {
            "score": mission["score"],
            "penalties": mission["penalties"],
            "outcomes": list(mission["outcome_log"]),
        }
        session["phase"] = "result_page"
        broadcast_mission_state(code, session)
        socketio.emit("mission_complete", session["mission_result"], room=code)
        return
    mission["status"] = "active"
    broadcast_mission_state(code, session)
