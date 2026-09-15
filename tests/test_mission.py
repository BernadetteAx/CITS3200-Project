from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.sockets.handlers import mission


@pytest.fixture
def mission_game(sample_session, monkeypatch):
    """Prepare a mission with a verified player and team inventory."""
    sample_session["phase"] = "mission"
    sample_session["players"]["player-1"]["socket_id"] = "socket-1"
    sample_session["players"]["player-2"]["socket_id"] = "socket-2"

    sample_session["purchased_items"] = [
        {"id": "axe", "name": "Axe"},
        {"id": "map", "name": "Map"},
        {"id": "fuel", "name": "Fuel"},
    ]

    monkeypatch.setattr(
        mission, "request", SimpleNamespace(sid="socket-1")
    )
    monkeypatch.setattr(mission, "emit", Mock())
    monkeypatch.setattr(mission.socketio, "emit", Mock())

    mission.initialise_mission(sample_session)
    return sample_session


def payload(item="axe", index=0, player="player-1"):
    return {
        "sessionCode": "ABCD",
        "playerId": player,
        "challengeIndex": index,
        "itemId": item,
    }


def test_initialise_mission_defaults(mission_game):
    state = mission_game["mission"]

    assert state["score"] == 100
    assert state["penalties"] == 0
    assert state["status"] == "active"
    assert state["current_challenge_index"] == 0
    assert state["used_items"] == []
    assert state["outcome_log"] == []
    assert state["outcome"] is None
    assert state["challenges"] == mission.CHALLENGES
    assert state["inventory"] == mission_game["purchased_items"]


def test_initialise_preserves_existing_progress(mission_game):
    state = mission_game["mission"]
    state["score"] = 90
    state["current_challenge_index"] = 1

    result = mission.initialise_mission(mission_game)

    assert result is state
    assert result["score"] == 90
    assert result["current_challenge_index"] == 1


def test_inventory_is_copied_from_purchases(mission_game):
    mission_game["mission"]["inventory"][0]["name"] = "Changed"

    assert mission_game["purchased_items"][0]["name"] == "Axe"


def test_initialise_without_purchases(sample_session):
    state = mission.initialise_mission(sample_session)

    assert state["inventory"] == []


def test_successful_item_records_success_without_penalty(mission_game):
    mission.mission_use_item(payload(item="axe"))

    state = mission_game["mission"]
    outcome = state["outcome"]

    assert state["status"] == "resolved"
    assert state["score"] == 100
    assert state["penalties"] == 0
    assert state["used_items"] == ["axe"]
    assert outcome["success"] is True
    assert outcome["penalty"] == 0
    assert outcome["challengeId"] == "wall"
    assert outcome["challengeIndex"] == 0
    assert outcome["item"]["id"] == "axe"
    assert outcome["description"]
    assert state["outcome_log"] == [outcome]

    mission.socketio.emit.assert_any_call(
        "mission_outcome", outcome, room="ABCD"
    )


def test_unsuitable_item_records_failure_and_penalty(mission_game):
    mission.mission_use_item(payload(item="map"))

    state = mission_game["mission"]

    assert state["status"] == "resolved"
    assert state["score"] == 90
    assert state["penalties"] == 10
    assert state["used_items"] == ["map"]
    assert state["outcome"]["success"] is False
    assert state["outcome"]["penalty"] == 10


def test_continue_without_item_applies_penalty(mission_game):
    mission.mission_continue(payload())

    state = mission_game["mission"]

    assert state["status"] == "resolved"
    assert state["score"] == 90
    assert state["penalties"] == 10
    assert state["used_items"] == []
    assert state["outcome"]["item"] is None
    assert state["outcome"]["success"] is False


def test_score_cannot_become_negative(mission_game):
    mission_game["mission"]["score"] = 5

    mission.mission_continue(payload())

    assert mission_game["mission"]["score"] == 0
    assert mission_game["mission"]["penalties"] == 10


def test_item_not_in_inventory_is_rejected(mission_game):
    mission.mission_use_item(payload(item="toolkit"))

    state = mission_game["mission"]
    assert state["status"] == "active"
    assert state["used_items"] == []
    assert state["outcome_log"] == []
    mission.socketio.emit.assert_not_called()


def test_used_item_cannot_be_reused(mission_game):
    mission.mission_use_item(payload(item="axe"))
    mission.mission_advance(payload())

    mission.mission_use_item(payload(item="axe", index=1))

    state = mission_game["mission"]
    assert state["status"] == "active"
    assert state["used_items"] == ["axe"]
    assert len(state["outcome_log"]) == 1


@pytest.mark.parametrize(
    "action",
    [mission.mission_use_item, mission.mission_continue],
)
def test_resolved_challenge_cannot_be_resolved_again(
    mission_game, action
):
    mission.mission_continue(payload())

    action(payload())

    state = mission_game["mission"]
    assert state["score"] == 90
    assert state["penalties"] == 10
    assert len(state["outcome_log"]) == 1


@pytest.mark.parametrize(
    "bad_payload",
    [
        None,
        {},
        "invalid",
        {"sessionCode": "MISSING"},
        payload(player="unknown"),
        payload(player="player-2"),  # Wrong sending socket.
        payload(index=99),
    ],
)
def test_action_session_rejects_invalid_requests(
    mission_game, bad_payload
):
    assert mission._action_session(bad_payload) == (
        None, None, None
    )


@pytest.mark.parametrize("phase", ["lobby", "auction", "result_page"])
def test_actions_rejected_outside_mission_phase(mission_game, phase):
    mission_game["phase"] = phase

    assert mission._action_session(payload()) == (
        None, None, None
    )


def test_actions_rejected_without_mission_state(mission_game):
    del mission_game["mission"]

    assert mission._action_session(payload()) == (
        None, None, None
    )


def test_valid_action_session_returns_game(mission_game):
    code, session, state = mission._action_session(payload())

    assert code == "ABCD"
    assert session is mission_game
    assert state is mission_game["mission"]


@pytest.mark.parametrize(
    "action, status",
    [
        (mission.mission_use_item, "active"),
        (mission.mission_continue, "active"),
        (mission.mission_advance, "resolved"),
    ],
)
def test_handlers_reject_another_players_socket(
    mission_game, action, status
):
    state = mission_game["mission"]
    state["status"] = status

    action(payload(player="player-2"))

    assert state["status"] == status
    assert state["current_challenge_index"] == 0
    assert state["outcome_log"] == []
    mission.socketio.emit.assert_not_called()


def test_advance_requires_resolved_challenge(mission_game):
    mission.mission_advance(payload())

    state = mission_game["mission"]
    assert state["current_challenge_index"] == 0
    assert state["status"] == "active"
    mission.socketio.emit.assert_not_called()


def test_advance_opens_next_challenge(mission_game):
    mission.mission_use_item(payload())
    mission.mission_advance(payload())

    state = mission_game["mission"]
    assert state["current_challenge_index"] == 1
    assert state["status"] == "active"
    assert state["outcome"] is None
    assert len(state["outcome_log"]) == 1
    assert state["used_items"] == ["axe"]


@pytest.mark.parametrize(
    "action",
    [
        mission.mission_use_item,
        mission.mission_continue,
        mission.mission_advance,
    ],
)
def test_delayed_previous_challenge_action_is_ignored(
    mission_game, action
):
    mission.mission_use_item(payload())
    mission.mission_advance(payload())
    mission.socketio.emit.reset_mock()

    action(payload(index=0))

    state = mission_game["mission"]
    assert state["current_challenge_index"] == 1
    assert state["status"] == "active"
    assert state["score"] == 100
    assert len(state["outcome_log"]) == 1
    mission.socketio.emit.assert_not_called()


def test_state_marks_used_items_without_changing_inventory(mission_game):
    mission.mission_use_item(payload(item="axe"))

    state = mission._state(mission_game)
    items = {item["id"]: item for item in state["inventory"]}

    assert items["axe"]["used"] is True
    assert items["map"]["used"] is False
    assert state["usedItems"] == ["axe"]
    assert state["totalChallenges"] == len(mission.CHALLENGES)
    assert all(
        "used" not in item
        for item in mission_game["mission"]["inventory"]
    )


def test_personal_state_is_emitted(mission_game):
    mission.emit_mission_state_to_player(mission_game)

    mission.emit.assert_called_once_with(
        "mission_state", mission._state(mission_game)
    )


def test_personal_state_not_emitted_without_mission(mission_game):
    del mission_game["mission"]

    mission.emit_mission_state_to_player(mission_game)

    mission.emit.assert_not_called()


def test_broadcast_targets_game_room(mission_game):
    mission.broadcast_mission_state("ABCD", mission_game)

    mission.socketio.emit.assert_called_once_with(
        "mission_state", mission._state(mission_game), room="ABCD"
    )


@pytest.mark.parametrize(
    "use_items, expected_score, expected_penalties",
    [
        (True, 100, 0),
        (False, 70, 30),
    ],
)
def test_completing_mission_records_final_results(
    mission_game, use_items, expected_score, expected_penalties
):
    # These items match the three placeholder challenges.
    for index, item in enumerate(["axe", "map", "fuel"]):
        data = payload(item=item, index=index)

        if use_items:
            mission.mission_use_item(data)
        else:
            mission.mission_continue(data)

        mission.mission_advance(data)

    state = mission_game["mission"]
    result = mission_game["mission_result"]

    assert state["status"] == "complete"
    assert state["current_challenge_index"] == 3
    assert state["outcome"] is None
    assert mission_game["phase"] == "result_page"
    assert result["score"] == expected_score
    assert result["penalties"] == expected_penalties
    assert len(result["outcomes"]) == 3
    assert result["outcomes"] == state["outcome_log"]
    assert result["outcomes"] is not state["outcome_log"]
    assert mission._state(mission_game)["challenge"] is None

    mission.socketio.emit.assert_any_call(
        "mission_complete", result, room="ABCD"
    )