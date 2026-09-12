from copy import deepcopy

import pytest

from app.services.scoring_service import build_result_state


@pytest.fixture
def completed_game():
    """A completed game containing one passed and one failed challenge."""
    axe = {"id": "axe", "name": "Axe", "cost": 20}
    map_item = {"id": "map", "name": "Map", "cost": 10}

    return {
        "phase": "result_page",
        "auction": {
            "budget": 70,
            "purchased_items": [dict(axe), dict(map_item)],
        },
        "purchased_items": [dict(axe), dict(map_item)],
        "mission": {
            "status": "complete",
            "challenges": [
                {"id": "wall", "name": "Scale the Wall"},
                {"id": "lost-route", "name": "Find the Safe Route"},
            ],
            "inventory": [dict(axe), dict(map_item)],
            "used_items": ["axe"],
            # Deliberately different to verify recorded results are used.
            "score": 100,
            "penalties": 0,
        },
        "mission_result": {
            "score": 90,
            "penalties": 10,
            "outcomes": [
                {
                    "challengeId": "wall",
                    "challengeIndex": 0,
                    "item": dict(axe),
                    "success": True,
                    "penalty": 0,
                    "title": "Obstacle Cleared",
                    "description": "The Axe gets the team past the challenge.",
                },
                {
                    "challengeId": "lost-route",
                    "challengeIndex": 1,
                    "item": None,
                    "success": False,
                    "penalty": 10,
                    "title": "Forced to Double Back",
                    "description": "No item was used.",
                },
            ],
        },
    }


@pytest.mark.parametrize("key", ["mission", "mission_result"])
def test_missing_required_state_returns_none(completed_game, key):
    del completed_game[key]

    assert build_result_state(completed_game) is None


@pytest.mark.parametrize("status", ["active", "resolved", None])
def test_unfinished_mission_returns_none(completed_game, status):
    completed_game["mission"]["status"] = status

    assert build_result_state(completed_game) is None


def test_missing_recorded_result_returns_none(completed_game):
    completed_game["mission_result"] = None

    assert build_result_state(completed_game) is None


def test_empty_session_returns_none():
    assert build_result_state({}) is None


def test_summary_uses_recorded_score_and_penalties(completed_game):
    result = build_result_state(completed_game)

    assert result["finalScore"] == 90
    assert result["totalPenalties"] == 10
    assert result["leftoverMoney"] == 70
    assert result["totalChallenges"] == 2
    assert result["challengesCompleted"] == 2
    assert result["challengesPassed"] == 1
    assert result["challengesFailed"] == 1
    assert result["completionStatus"] == "complete"
    assert result["missionOutcome"] is None


def test_challenge_details_are_mapped_correctly(completed_game):
    result = build_result_state(completed_game)

    assert result["challenges"][0] == {
        "challengeId": "wall",
        "challengeIndex": 0,
        "name": "Scale the Wall",
        "success": True,
        "penalty": 0,
        "title": "Obstacle Cleared",
        "description": "The Axe gets the team past the challenge.",
        "itemUsed": {"id": "axe", "name": "Axe", "cost": 20},
    }


def test_challenge_without_item_displays_none(completed_game):
    result = build_result_state(completed_game)

    assert result["challenges"][1]["itemUsed"] is None


def test_optional_outcome_details_have_defaults(completed_game):
    outcome = completed_game["mission_result"]["outcomes"][0]
    for key in ("item", "title", "description"):
        del outcome[key]

    challenge = build_result_state(completed_game)["challenges"][0]

    assert challenge["itemUsed"] is None
    assert challenge["title"] == ""
    assert challenge["description"] == ""


@pytest.mark.parametrize("index", [-1, 99])
def test_invalid_challenge_index_uses_fallback_name(
    completed_game, index
):
    completed_game["mission_result"]["outcomes"][0][
        "challengeIndex"
    ] = index

    challenge = build_result_state(completed_game)["challenges"][0]

    assert challenge["name"] == f"Challenge {index + 1}"


def test_missing_challenge_name_uses_fallback(completed_game):
    del completed_game["mission"]["challenges"][0]["name"]

    result = build_result_state(completed_game)

    assert result["challenges"][0]["name"] == "Challenge 1"


def test_missing_challenge_list_uses_fallbacks(completed_game):
    del completed_game["mission"]["challenges"]

    result = build_result_state(completed_game)

    assert result["totalChallenges"] == 0
    assert result["challengesCompleted"] == 2
    assert result["challenges"][0]["name"] == "Challenge 1"
    assert result["challenges"][1]["name"] == "Challenge 2"


@pytest.mark.parametrize(
    "successes, passed, failed",
    [
        ([True, True], 2, 0),
        ([False, False], 0, 2),
        ([True, False], 1, 1),
    ],
)
def test_passed_and_failed_counts(
    completed_game, successes, passed, failed
):
    for outcome, success in zip(
        completed_game["mission_result"]["outcomes"], successes
    ):
        outcome["success"] = success

    result = build_result_state(completed_game)

    assert result["challengesPassed"] == passed
    assert result["challengesFailed"] == failed


def test_no_outcomes_produces_empty_challenge_results(completed_game):
    completed_game["mission_result"]["outcomes"] = []

    result = build_result_state(completed_game)

    assert result["challenges"] == []
    assert result["challengesCompleted"] == 0
    assert result["challengesPassed"] == 0
    assert result["challengesFailed"] == 0


def test_zero_score_and_budget_are_preserved(completed_game):
    completed_game["mission_result"]["score"] = 0
    completed_game["auction"]["budget"] = 0

    result = build_result_state(completed_game)

    assert result["finalScore"] == 0
    assert result["leftoverMoney"] == 0


def test_session_purchases_take_priority_over_auction(completed_game):
    completed_game["purchased_items"] = [
        {"id": "fuel", "name": "Fuel"}
    ]

    result = build_result_state(completed_game)

    assert result["itemsPurchased"] == [
        {"id": "fuel", "name": "Fuel"}
    ]


def test_empty_session_purchases_do_not_use_auction_fallback(
    completed_game,
):
    completed_game["purchased_items"] = []

    result = build_result_state(completed_game)

    assert result["itemsPurchased"] == []


def test_purchases_fall_back_to_auction(completed_game):
    del completed_game["purchased_items"]

    result = build_result_state(completed_game)

    assert result["itemsPurchased"] == completed_game["auction"][
        "purchased_items"
    ]


def test_missing_auction_and_purchases_have_defaults(completed_game):
    del completed_game["auction"]
    del completed_game["purchased_items"]

    result = build_result_state(completed_game)

    assert result["leftoverMoney"] is None
    assert result["itemsPurchased"] == []


def test_used_items_follow_recorded_order(completed_game):
    completed_game["mission"]["used_items"] = ["map", "axe"]

    result = build_result_state(completed_game)

    assert result["itemsUsed"] == [
        {"id": "map", "name": "Map", "cost": 10},
        {"id": "axe", "name": "Axe", "cost": 20},
    ]


def test_unknown_used_item_has_fallback_name(completed_game):
    completed_game["mission"]["used_items"] = ["unknown-item"]

    result = build_result_state(completed_game)

    assert result["itemsUsed"] == [
        {"id": "unknown-item", "name": "unknown-item"}
    ]


def test_missing_inventory_uses_item_id_as_name(completed_game):
    del completed_game["mission"]["inventory"]

    result = build_result_state(completed_game)

    assert result["itemsUsed"] == [{"id": "axe", "name": "axe"}]


def test_missing_used_items_returns_empty_list(completed_game):
    del completed_game["mission"]["used_items"]

    result = build_result_state(completed_game)

    assert result["itemsUsed"] == []


def test_building_results_does_not_modify_session(completed_game):
    original = deepcopy(completed_game)

    build_result_state(completed_game)

    assert completed_game == original


def test_result_item_edits_do_not_change_source_items(completed_game):
    original = deepcopy(completed_game)
    result = build_result_state(completed_game)

    result["challenges"][0]["itemUsed"]["name"] = "Changed"
    result["itemsPurchased"][0]["name"] = "Changed"
    result["itemsUsed"][0]["name"] = "Changed"

    assert completed_game == original