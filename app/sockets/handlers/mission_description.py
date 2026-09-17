from flask_socketio import emit

from app.extensions import socketio
from app.game_data.get_random_mission import get_mission
from app.sockets.sessions import get_session


def _valid_player(session, payload):
    if not isinstance(payload, dict):
        return None

    player_id = payload.get("playerId")

    if player_id not in session.get("players", {}):
        return None

    return player_id


@socketio.on("begin_mission_description")
def begin_mission_description(payload):
    code = payload.get("sessionCode") if isinstance(payload, dict) else None
    session = get_session(code)

    if (
        not session
        or not _valid_player(session, payload)
        or payload["playerId"] != session["host_id"]
        or session["phase"] != "start_game"
    ):
        return

    # Generate the mission once and save it for the whole game.
    if not session.get("generated_mission"):
        session["generated_mission"] = get_mission()

    session["phase"] = "mission_description"

    emit("mission_description_started", room=code)


@socketio.on("get_mission_description")
def get_mission_description(payload):
    code = payload.get("sessionCode") if isinstance(payload, dict) else None
    session = get_session(code)

    player_id = _valid_player(session, payload) if session else None

    if (
        not session
        or not player_id
        or session["phase"] != "mission_description"
    ):
        return

    mission = session.get("generated_mission")

    if not mission:
        return

    emit(
        "mission_description_state",
        {
            "mission": mission["mission"],
            "location": mission["location"],
            "description": mission.get("mission_description", mission.get("mission_desc", "")),
            "isHost": player_id == session["host_id"],
        }
    )
    