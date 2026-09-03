""" THIS NEEDS TO BE REVIEWED AFTER THE MISSIONS ARE SUBMITTED
Authoritative Socket.IO state and actions for the mission phase
Angela have fun with this file some fake challenges are here for now
please make sure preoper missions and stuff are pulled from the correct spot later"""

from flask import request
from flask_socketio import emit

from app.extensions import socketio
from app.sockets.sessions import get_session


# challenge data and the matching item stay on the server
#challenges are generated rn
CHALLENGES = [
    {"id": "wall", "name": "Scale the Wall", "description": "A sheer stone wall blocks the only route forward.", "image": "icons8-mountain-64.png", "success_items": ["axe", "mountain-gear", "toolkit"]},
    {"id": "lost-route", "name": "Find the Safe Route", "description": "The route markers have vanished in thick fog.", "image": "icons8-map-64.png", "success_items": ["map", "gps", "compass"]},
    {"id": "broken-vehicle", "name": "Keep Moving", "description": "Your vehicle stalls before the final stretch.", "image": "icons8-sedan-64.png", "success_items": ["toolkit", "fuel", "car", "credit-card"]},
]


def initialise_mission(session):
    """Create mission state once, retaining the auction's team inventory."""
    if not session.get("mission"):
        session["mission"] = {"challenges": [dict(c) for c in CHALLENGES], "current_challenge_index": 0,
            "inventory": [dict(item) for item in session.get("purchased_items", [])], "used_items": [],
            "outcome_log": [], "score": 100, "penalties": 0, "status": "active", "outcome": None}
    return session["mission"]


def _valid_player(session, payload):
    if not isinstance(payload, dict) or not payload.get("sessionCode"):
        return None
    player_id = payload.get("playerId")
    player = session["players"].get(player_id)
    #playerId must belong to the sending socket
    if not player or player.get("socket_id") != request.sid:
        return None
    return player_id


def _state(session):
    mission = session["mission"]
    index = mission["current_challenge_index"]
    current = mission["challenges"][index] if index < len(mission["challenges"]) else None
    used = set(mission["used_items"])
    inventory = [{**item, "used": item["id"] in used} for item in mission["inventory"]]
    return {"phase": session["phase"], "missionName": "The Heist", "currentChallengeIndex": index,
        "totalChallenges": len(mission["challenges"]), "challenge": current, "inventory": inventory,
        "usedItems": list(mission["used_items"]), "outcomeLog": list(mission["outcome_log"]),
        "score": mission["score"], "penalties": mission["penalties"], "status": mission["status"], "outcome": mission["outcome"]}


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
    # binding actions to the rendered challenge stops delayed duplicates from changing a later challenge
    if not player or payload.get("challengeIndex") != mission["current_challenge_index"]:
        return None, None, None
    return code, session, mission


def _resolve(code, session, mission, item=None):
    challenge = mission["challenges"][mission["current_challenge_index"]]
    if item:
        mission["used_items"].append(item["id"])
        successful = item["id"] in challenge["success_items"]
        title = "Obstacle Cleared" if successful else "A Costly Detour"
        description = f"The {item['name']} gets the team past the challenge." if successful else f"The {item['name']} was not enough; the team takes a longer route."
    else:
        successful, title, description = False, "Forced to Double Back", "No item was used, so the team took the longer route."
    penalty = 0 if successful else 10
    mission["penalties"] += penalty
    mission["score"] = max(0, mission["score"] - penalty)
    outcome = {"challengeId": challenge["id"], "challengeIndex": mission["current_challenge_index"], "item": item,
        "success": successful, "penalty": penalty, "title": title, "description": description}
    mission["outcome"] = outcome
    mission["outcome_log"].append(outcome)
    mission["status"] = "resolved"
    broadcast_mission_state(code, session)
    socketio.emit("mission_outcome", outcome, room=code)


@socketio.on("mission_use_item")
def mission_use_item(payload):
    code, session, mission = _action_session(payload)
    if not session or mission["status"] != "active": return
    item_id = payload.get("itemId")
    item = next((item for item in mission["inventory"] if item["id"] == item_id), None)
    if not item or item_id in mission["used_items"]: return
    _resolve(code, session, mission, item)


@socketio.on("mission_continue")
def mission_continue(payload):
    code, session, mission = _action_session(payload)
    if session and mission["status"] == "active": _resolve(code, session, mission)


@socketio.on("mission_advance")
def mission_advance(payload):
    code, session, mission = _action_session(payload)
    if not session or mission["status"] != "resolved": return
    mission["current_challenge_index"] += 1
    mission["outcome"] = None
    if mission["current_challenge_index"] >= len(mission["challenges"]):
        mission["status"] = "complete"
        session["mission_result"] = {"score": mission["score"], "penalties": mission["penalties"], "outcomes": list(mission["outcome_log"])}
        session["phase"] = "result_page"
        broadcast_mission_state(code, session)
        socketio.emit("mission_complete", session["mission_result"], room=code)
        return
    mission["status"] = "active"
    broadcast_mission_state(code, session)
