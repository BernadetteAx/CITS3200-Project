"""The briefing, equipment shop and mission must use the same generated data."""
from unittest.mock import Mock

import pytest

from app.game_data import get_random_mission
from app.game_data.mission_structs import missions_list
from app.sockets.handlers.auction import initialise_auction
from app.sockets.handlers.mission import initialise_mission, _state


MISSION_LOCATIONS = [
    (mission, location)
    for mission in missions_list
    for location in mission["location_options"]
]


@pytest.mark.parametrize("template,location", MISSION_LOCATIONS,
                         ids=[f"{m['mission_name']}-{loc}" for m, loc in MISSION_LOCATIONS])
def test_generated_briefing_survives_shop_to_mission_transition(
    sample_session, monkeypatch, template, location
):
    options = [mission for mission in missions_list if location in mission["location_options"]]
    monkeypatch.setattr(get_random_mission.random, "randint", Mock(side_effect=[
        get_random_mission.possible_locations.index(location),
        options.index(template), 0, 0, 0, 0, 0, 0,
    ]))
    generated = get_random_mission.get_mission()
    auction = initialise_auction(sample_session, generated)
    offered_names = {item["name"] for pair in auction["item_pairs"] for item in pair}
    for index in range(1, 7):
        assert offered_names.intersection(generated[f"challenge_{index}"]["items"])

    sample_session["purchased_items"] = [dict(auction["item_pairs"][0][0])]
    initialise_mission(sample_session, generated)
    sample_session["phase"] = "mission"
    state = _state(sample_session)

    assert state["missionName"] == generated["mission"]
    assert state["missionDescription"] == generated["mission_description"]
    assert state["location"] == location
    assert state["totalChallenges"] == 6
    assert state["inventory"][0]["name"] in offered_names
    assert [c["name"] for c in sample_session["mission"]["challenges"]] == [
        generated[f"challenge_{index}"]["challenge_name"] for index in range(1, 7)
    ]
    assert [c["type"] for c in sample_session["mission"]["challenges"]] == [
        template[f"challenge_{index}"] for index in range(1, 7)
    ]
    for challenge in sample_session["mission"]["challenges"]:
        assert challenge["description"].lower() not in {"incomplete", "imcomplete"}
        assert "insert_item_here" not in challenge["description"]


def test_missing_or_placeholder_descriptions_get_fallback_text(sample_session):
    generated = {
        "mission": "Fallback Mission",
        "location": "The Docks",
        "mission_description": "A quiet evening on the waterfront.",
    }
    for index in range(1, 7):
        generated[f"challenge_{index}"] = {
            "challenge_name": f"Challenge {index}",
            "desc": "Incomplete" if index == 2 else "" if index == 4 else "The team needs insert_item_here to continue.",
            "items": {},
            "failure_items": {},
        }

    sample_session["purchased_items"] = [{"id": "axe", "name": "Axe"}]
    initialise_mission(sample_session, generated)

    challenges = sample_session["mission"]["challenges"]
    assert "Your crew faces Challenge 2" in challenges[1]["description"]
    assert "Your crew faces Challenge 4" in challenges[3]["description"]
    assert "insert_item_here" not in challenges[2]["description"]
    assert all(challenge["description"] for challenge in challenges)
    assert all(
        "incomplete" not in challenge["description"].lower()
        for challenge in challenges
    )
