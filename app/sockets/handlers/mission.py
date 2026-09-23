"""Authoritative Socket.IO state and actions for the generated mission phase."""

from flask import request
from flask_socketio import emit

from app.extensions import socketio
from app.game_data.example_mission import example_mission
from app.sockets.sessions import get_session


# Challenge Card Detail - START
# game_data uses "Incomplete" (and a misspelt "Imcomplete") as a placeholder
# for copy that has not been written yet. Treat those as absent so the UI
# falls back instead of printing the placeholder to players.
def _usable_text(value):
    text = (value or "").strip()
    if not text or text.lower() in {"incomplete", "imcomplete"}:
        return None
    return text
# Challenge Card Detail - END


def _normalise_challenges(generated_mission):
    challenges = []
    for index in range(1, 7):
        challenge = generated_mission[f"challenge_{index}"]
        name = challenge["challenge_name"]
        description = (challenge.get("desc") or "").strip()
        if not description or description.lower() in {"incomplete", "imcomplete"}:
            description = f"Your crew faces {name}. Check your equipment and choose how to continue. Taking the long way round costs your team points."
        description = description.replace("insert_item_here", "mission objective")
        weight = generated_mission[f"w{index}"]
        challenges.append({
            "id": f"challenge-{index}",
            "name": name,
            "type": challenge.get("type", ""),
            "description": description,
            "weight": weight,
            "image": "icons8-about-64.png",
            # Dict keyed by item name so _resolve can look up point_value.
            # (Restored after a merge resolution reverted this to a list,
            # which made every mission_use_item crash on .get().)
            "success_items": {
                item_name: dict(item_result)
                for item_name, item_result in challenge.get("items", {}).items()
            },
            
            "failure_items": {
                item_name: dict(item_result)
                for item_name, item_result in challenge.get("failure_items", {}).items()
            },
            # Challenge Card Detail - START
            # Keep each item's point copy from game_data so the results card can
            # show the real outcome text and point value. Display only: no score
            # or penalty is derived from this, and success is still decided by
            # success_items above, so merging failure_items here is safe.
            "item_effects": {
                item_name: {
                    "point_value": effect.get("point_value"),
                    "point_desc": _usable_text(effect.get("point_desc")),
                }
                for source in ("items", "failure_items")
                for item_name, effect in (challenge.get(source) or {}).items()
                if isinstance(effect, dict)
            },
            # Challenge Card Detail - END
        })
    return challenges


def initialise_mission(session, generated_mission=None):
    """Create game-data mission state once, retaining the auction inventory."""
    if not session.get("mission"):
        generated_mission = generated_mission or example_mission
        session["mission"] = {"mission_name": generated_mission["mission"],
            "location": generated_mission.get("location", ""),
            "mission_description": generated_mission.get("mission_description", generated_mission.get("mission_desc", "")),
            "challenges": _normalise_challenges(generated_mission), "current_challenge_index": 0,
            "inventory": [dict(item) for item in session.get("purchased_items", [])], "used_items": [],
            "outcome_log": [], "score": 0, "penalties": 0, "status": "active", "outcome": None}
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
    return {"phase": session["phase"], "missionName": mission["mission_name"], "location": mission.get("location", ""),
        "missionDescription": mission["mission_description"], "currentChallengeIndex": index,
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


def _resolve(code, session, mission, item=None, timed_out=False):

    challenge = mission["challenges"][mission["current_challenge_index"]]
    instant_failure = False

    if item:
        mission["used_items"].append(item["id"])

        item_result = challenge["success_items"].get(item["name"])
        failure_result = challenge["failure_items"].get(item["name"])

        successful = item_result is not None
        instant_failure = failure_result is not None

        if successful:
            points_earned = int(item_result.get("point_value", 50)) * float(challenge.get("weight", 1))
            title = "Obstacle Cleared"
            description = (
                _usable_text(item_result.get("use_desc"))
                or f"The {item['name']} gets the team past the challenge."
            )

        elif instant_failure:
            points_earned = int(failure_result.get("point_value", 0))
            title = "Mission Failed"
            description = (
                _usable_text(failure_result.get("use_desc"))
                or f"Using the {item['name']} caused the mission to fail."
            )

        else:
            points_earned = 0
            title = "A Costly Detour"
            description = (
                f"The {item['name']} was not enough; "
                "the team takes a longer route."
            )

    elif timed_out:
        successful = False
        points_earned = 0
        title = "Time Ran Out"
        description = (
            "The team ran out of time and had to take the longer route."
        )

    else:
        successful = False
        points_earned = 0
        title = "Forced to Double Back"
        description = (
            "No item was used, so the team took the longer route."
        )

    # Normal failures count towards the three-failure limit.
    # A failure_item ends the mission immediately instead.
    penalty = 0

    if not successful and not instant_failure:
        penalty = 1
        mission["penalties"] += 1

    mission["score"] += points_earned

    # Challenge Card Detail - START
    effect = (
        (challenge.get("item_effects") or {}).get(item["name"])
        if item else None
    )
    point_desc = (effect or {}).get("point_desc")
    point_value = ((effect or {}).get("point_value"))
    # Challenge Card Detail - END

    outcome = {
        "challengeId": challenge["id"],
        "challengeIndex": mission["current_challenge_index"],
        "item": item,
        "success": successful,
        "pointsEarned": points_earned,
        "penalty": penalty,
        "title": title,
        "description": description,
        "pointDesc": point_desc,
        "pointValue": (point_value * float(challenge.get("weight", 1)))
    }

    mission["outcome"] = outcome
    mission["outcome_log"].append(outcome)

    # A failure item immediately ends the mission.
    if instant_failure:
        mission["status"] = "complete"

        session["mission_result"] = {
            "score": mission["score"],
            "penalties": mission["penalties"],
            "outcomes": list(mission["outcome_log"])
        }

        session["phase"] = "result_page"

        broadcast_mission_state(code, session)
        socketio.emit("mission_outcome", outcome, room=code)
        socketio.emit(
            "mission_complete",
            session["mission_result"],
            room=code
        )

        return

    # Three normal failed challenges ends the mission.
    if mission["penalties"] >= 3:
        mission["status"] = "complete"

        session["mission_result"] = {
            "score": mission["score"],
            "penalties": mission["penalties"],
            "outcomes": list(mission["outcome_log"])
        }

        session["phase"] = "result_page"

        broadcast_mission_state(code, session)
        socketio.emit("mission_outcome", outcome, room=code)
        socketio.emit(
            "mission_complete",
            session["mission_result"],
            room=code
        )
        return

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

@socketio.on("mission_timeout")
def mission_timeout(payload):
    code, session, mission = _action_session(payload)
    if session and mission["status"] == "active": _resolve(code, session, mission, timed_out=True)


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
