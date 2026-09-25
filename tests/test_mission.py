from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.sockets.handlers import mission


# ---------------------------------------------------------------------------
# Fixtures and test helpers
# ---------------------------------------------------------------------------


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
    sample_session["mission"]["challenges"][0]["success_items"]["Axe"] = {
        "point_value": 35,
    }
    sample_session["mission"]["challenges"][0]["item_effects"]["Axe"] = {
        "point_value": 35,
        "point_desc": "A reliable tool for this challenge.",
    }
    return sample_session


def payload(item="axe", index=0, player="player-1"):
    return {
        "sessionCode": "ABCD",
        "playerId": player,
        "challengeIndex": index,
        "itemId": item,
    }


# ---------------------------------------------------------------------------
# Mission setup and initial state
# ---------------------------------------------------------------------------


def test_initialise_mission_defaults(mission_game):
    state = mission_game["mission"]

    assert state["score"] == 0
    assert state["penalties"] == 0
    assert state["status"] == "active"
    assert state["current_challenge_index"] == 0
    assert state["used_items"] == []
    assert state["outcome_log"] == []
    assert state["outcome"] is None
    assert len(state["challenges"]) == 6
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


# ---------------------------------------------------------------------------
# Challenge resolution and item use
# ---------------------------------------------------------------------------


def test_successful_item_records_adds_its_point_value(mission_game):
    mission.mission_use_item(payload(item="axe"))

    state = mission_game["mission"]
    outcome = state["outcome"]

    assert state["status"] == "resolved"
    assert state["score"] == 35
    assert state["penalties"] == 0
    assert state["used_items"] == ["axe"]
    assert outcome["success"] is True
    assert outcome["penalty"] == 0
    assert outcome["challengeId"] == "challenge-1"
    assert outcome["challengeIndex"] == 0
    assert outcome["item"]["id"] == "axe"
    assert outcome["pointsEarned"] == 35
    assert outcome["pointValue"] == 35
    assert outcome["pointDesc"] == "A reliable tool for this challenge."
    assert outcome["description"]
    assert state["outcome_log"] == [outcome]

    mission.socketio.emit.assert_any_call(
        "mission_outcome", outcome, room="ABCD"
    )


def test_unsuitable_item_does_not_add_points_or_penalty(mission_game):
    mission.mission_use_item(payload(item="map"))

    state = mission_game["mission"]

    assert state["status"] == "resolved"
    assert state["score"] == 0
    assert state["penalties"] == 1
    assert state["used_items"] == ["map"]
    assert state["outcome"]["success"] is False
    assert state["outcome"]["penalty"] == 1
    assert state["outcome"]["pointsEarned"] == 0


def test_continue_without_item_does_not_change_score_or_penalty(mission_game):
    mission.mission_continue(payload())

    state = mission_game["mission"]

    assert state["status"] == "resolved"
    assert state["score"] == 0
    assert state["penalties"] == 1
    assert state["used_items"] == []
    assert state["outcome"]["item"] is None
    assert state["outcome"]["success"] is False


def test_continue_does_not_reduce_existing_score(mission_game):
    mission_game["mission"]["score"] = 5

    mission.mission_continue(payload())

    assert mission_game["mission"]["score"] == 5
    assert mission_game["mission"]["penalties"] == 1


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


def test_failure_item_immediately_ends_the_mission(mission_game):
    mission_game["mission"]["challenges"][0]["failure_items"] = {
        "Axe": {"point_value": 0, "use_desc": "The axe breaks and the team fails."}
    }
    mission_game["mission"]["challenges"][0]["success_items"] = {}

    mission.mission_use_item(payload(item="axe"))

    state = mission_game["mission"]
    assert state["status"] == "complete"
    assert mission_game["phase"] == "result_page"
    assert state["outcome"]["success"] is False
    assert state["outcome"]["penalty"] == 0
    assert state["outcome"]["title"] == "Mission Failed"
    assert mission_game["mission_result"]["outcomes"] == state["outcome_log"]
    mission.socketio.emit.assert_any_call(
        "mission_complete", mission_game["mission_result"], room="ABCD"
    )


# ---------------------------------------------------------------------------
# Request validation and action gating
# ---------------------------------------------------------------------------


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
    assert state["score"] == 0
    assert state["penalties"] == 1
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


# ---------------------------------------------------------------------------
# Challenge progression and round advancement
# ---------------------------------------------------------------------------


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
    assert state["score"] == 35
    assert len(state["outcome_log"]) == 1
    mission.socketio.emit.assert_not_called()


# ---------------------------------------------------------------------------
# State payloads and UI-facing output
# ---------------------------------------------------------------------------


def test_state_marks_used_items_without_changing_inventory(mission_game):
    mission.mission_use_item(payload(item="axe"))

    state = mission._state(mission_game)
    items = {item["id"]: item for item in state["inventory"]}

    assert items["axe"]["used"] is True
    assert items["map"]["used"] is False
    assert state["usedItems"] == ["axe"]
    assert state["totalChallenges"] == 6
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


def test_state_contains_current_challenge_description(mission_game):
    state = mission._state(mission_game)

    assert state["challenge"] is not None
    assert state["challenge"]["description"]
    assert isinstance(state["challenge"]["description"], str)


def test_state_contains_owned_inventory(mission_game):
    state = mission._state(mission_game)

    inventory_ids = {item["id"] for item in state["inventory"]}

    assert inventory_ids == {"axe", "map", "fuel"}


# ---------------------------------------------------------------------------
# Mission completion and final results
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "use_items, expected_score, expected_penalties, expected_index, expected_outcomes",
    [
        (True, 35, 3, 3, 4),
        (False, 0, 3, 2, 3),
    ],
)
def test_completing_mission_records_final_results(
    mission_game,
    use_items,
    expected_score,
    expected_penalties,
    expected_index,
    expected_outcomes,
):
    for index in range(6):
        data = payload(item="axe", index=index)

        if use_items and index == 0:
            mission.mission_use_item(data)
        else:
            mission.mission_continue(data)

        mission.mission_advance(data)

    state = mission_game["mission"]
    result = mission_game["mission_result"]

    assert state["status"] == "complete"
    assert state["current_challenge_index"] == expected_index
    assert state["outcome"] is not None
    assert mission_game["phase"] == "result_page"
    assert result["score"] == expected_score
    assert result["penalties"] == expected_penalties
    assert len(result["outcomes"]) == expected_outcomes
    assert result["outcomes"] == state["outcome_log"]
    assert result["outcomes"] is not state["outcome_log"]
    assert mission._state(mission_game)["challenge"]["id"] == (
        f"challenge-{expected_index + 1}"
    )

    mission.socketio.emit.assert_any_call(
        "mission_complete", result, room="ABCD"
    )


# ---------------------------------------------------------------------------
# Timeout handling and edge-case completion signals
# ---------------------------------------------------------------------------


def test_mission_timeout_fails_challenge_and_applies_penalty(mission_game):
    mission.mission_timeout(payload())

    state = mission_game["mission"]
    outcome = state["outcome"]

    assert state["status"] == "resolved"
    assert state["penalties"] == 1
    assert state["score"] == 0

    assert outcome["success"] is False
    assert outcome["item"] is None
    assert outcome["pointsEarned"] == 0
    assert outcome["penalty"] == 1
    assert outcome["title"] == "Time Ran Out"


def test_timeout_cannot_resolve_already_resolved_challenge(mission_game):
    mission.mission_timeout(payload())

    outcome_count = len(mission_game["mission"]["outcome_log"])

    mission.mission_timeout(payload())

    assert mission_game["mission"]["status"] == "resolved"
    assert len(mission_game["mission"]["outcome_log"]) == outcome_count
    assert mission_game["mission"]["penalties"] == 1


def test_timeout_broadcasts_outcome(mission_game):
    mission.mission_timeout(payload())

    outcome = mission_game["mission"]["outcome"]

    mission.socketio.emit.assert_any_call(
        "mission_outcome",
        outcome,
        room="ABCD",
    )


# ---------------------------------------------------------------------------
# Challenge text sanitisation and edge-case data cleanup
# ---------------------------------------------------------------------------


def test_normalise_challenges_replaces_placeholder_text():
    generated = {
        f"challenge_{index}": {
            "challenge_name": f"Challenge {index}",
            "desc": "Incomplete" if index == 1 else "",
            "items": {},
            "failure_items": {},
        }
        for index in range(1, 7)
    }
    generated["challenge_2"]["desc"] = (
        "The team needs insert_item_here to continue."
    )

    normalised = mission._normalise_challenges(generated)

    assert len(normalised) == 6
    assert "Your crew faces Challenge 1" in normalised[0]["description"]
    assert "mission objective" in normalised[1]["description"]
    assert "insert_item_here" not in normalised[1]["description"]
    assert all(challenge["description"] for challenge in normalised)
    assert all("incomplete" not in challenge["description"].lower() for challenge in normalised)
