from unittest.mock import Mock

import pytest

from app.sockets.handlers import auction


@pytest.fixture
def auction_game(sample_session, monkeypatch):
    """Create an auction and prevent real socket/timer activity."""
    sample_session["phase"] = "auction"
    auction.initialise_auction(sample_session)

    monkeypatch.setattr(auction, "emit", Mock())
    monkeypatch.setattr(auction.socketio, "emit", Mock())
    monkeypatch.setattr(
        auction.socketio, "start_background_task", Mock()
    )
    monkeypatch.setattr(auction.socketio, "sleep", Mock())

    return sample_session


@pytest.fixture
def voting_game(auction_game):
    auction._start_round("ABCD", auction_game)
    return auction_game


def payload(player="player-1", item="axe", code="ABCD"):
    return {
        "sessionCode": code,
        "playerId": player,
        "itemId": item,
    }


def test_initialise_auction(auction_game):
    state = auction_game["auction"]

    assert state["budget"] == 1000
    assert state["round_index"] == 0
    assert state["status"] == "waiting"
    assert state["votes"] == {}
    assert state["finished_players"] == set()
    assert state["purchased_items"] == []
    assert state["current_item_pair"] == list(
        auction.ITEM_PAIRS[0]
    )


def test_initialise_preserves_existing_auction(auction_game):
    state = auction_game["auction"]
    state["budget"] = 75

    result = auction.initialise_auction(auction_game)

    assert result is state
    assert result["budget"] == 75


def test_host_can_begin_auction(auction_game):
    auction_game["phase"] = "start_game"

    auction.begin_auction(payload())

    assert auction_game["phase"] == "auction"
    assert auction_game["auction"]["status"] == "voting"
    auction.emit.assert_called_with(
        "auction_started", room="ABCD"
    )


@pytest.mark.parametrize(
    "player, phase",
    [
        ("player-2", "start_game"),
        ("unknown", "start_game"),
        ("player-1", "lobby"),
        ("player-1", "mission"),
        ("player-1", "auction"),
    ],
)
def test_invalid_start_is_ignored(auction_game, player, phase):
    auction_game["phase"] = phase

    auction.begin_auction(payload(player=player))

    assert auction_game["phase"] == phase
    assert auction_game["auction"]["status"] == "waiting"
    auction.socketio.start_background_task.assert_not_called()


@pytest.mark.parametrize(
    "event",
    [
        auction.begin_auction,
        auction.auction_vote,
        auction.auction_skip,
        auction.auction_finish_voting,
        auction.resolve_auction_round,
    ],
)
@pytest.mark.parametrize(
    "data",
    [None, {}, "invalid", {"sessionCode": "MISSING"}],
)
def test_missing_or_invalid_session_is_ignored(
    auction_game, event, data
):
    event(data)

    assert auction_game["auction"]["status"] == "waiting"
    auction.socketio.emit.assert_not_called()
    auction.emit.assert_not_called()


def test_start_round_resets_previous_round(
    auction_game, monkeypatch
):
    monkeypatch.setattr(auction.time, "time", lambda: 1000)
    state = auction_game["auction"]
    state.update({
        "votes": {"player-1": "axe"},
        "finished_players": {"player-1"},
        "round_result": {"type": "tie"},
        "timer_token": 4,
    })

    auction._start_round("ABCD", auction_game)

    assert state["votes"] == {}
    assert state["finished_players"] == set()
    assert state["round_result"] is None
    assert state["status"] == "voting"
    assert state["ends_at"] == 1000 + auction.ROUND_SECONDS
    assert state["timer_token"] == 5
    auction.socketio.start_background_task.assert_called_once_with(
        auction._timer, "ABCD", 5
    )


def test_player_can_vote_and_change_vote(voting_game):
    auction.auction_vote(payload(item="axe"))
    assert voting_game["auction"]["votes"]["player-1"] == "axe"

    auction.auction_vote(payload(item="water-bottle"))
    assert voting_game["auction"]["votes"] == {
        "player-1": "water-bottle"
    }


@pytest.mark.parametrize(
    "player, item",
    [
        ("unknown", "axe"),
        ("player-1", "not-an-item"),
        ("player-1", "shovel"),  # Belongs to a later round.
        ("player-1", "skip"),    # Uses a separate event.
    ],
)
def test_invalid_vote_is_ignored(voting_game, player, item):
    auction.auction_vote(payload(player=player, item=item))

    assert voting_game["auction"]["votes"] == {}


def test_finished_player_cannot_change_vote(voting_game):
    auction.auction_vote(payload())
    auction.auction_finish_voting(payload())

    auction.auction_vote(payload(item="water-bottle"))

    assert voting_game["auction"]["votes"]["player-1"] == "axe"


def test_vote_outside_voting_status_is_ignored(auction_game):
    auction.auction_vote(payload())

    assert auction_game["auction"]["votes"] == {}


def test_finish_without_vote_is_ignored(voting_game):
    auction.auction_finish_voting(payload())

    assert voting_game["auction"]["finished_players"] == set()
    assert voting_game["auction"]["status"] == "voting"


def test_one_finished_player_does_not_resolve(voting_game):
    auction.auction_vote(payload())
    auction.auction_finish_voting(payload())

    assert voting_game["auction"]["finished_players"] == {
        "player-1"
    }
    assert voting_game["auction"]["status"] == "voting"


def test_all_finished_players_resolve_round(voting_game):
    for player in ("player-1", "player-2"):
        auction.auction_vote(payload(player=player))
        auction.auction_finish_voting(payload(player=player))

    state = voting_game["auction"]
    assert state["status"] == "resolved"
    assert state["round_result"]["type"] == "purchase"
    assert state["round_result"]["reason"] == "all_finished"
    assert state["purchased_items"][0]["id"] == "axe"


def test_skip_replaces_vote_and_finishes_player(voting_game):
    auction.auction_vote(payload())

    auction.auction_skip(payload())

    assert voting_game["auction"]["votes"]["player-1"] == "skip"
    assert "player-1" in voting_game["auction"]["finished_players"]


def test_finished_player_cannot_replace_vote_with_skip(voting_game):
    auction.auction_vote(payload())
    auction.auction_finish_voting(payload())

    auction.auction_skip(payload())

    assert voting_game["auction"]["votes"]["player-1"] == "axe"


@pytest.mark.parametrize(
    "votes, budget, expected_type, expected_budget, expected_ids",
    [
        (
            {"player-1": "axe", "player-2": "axe"},
            100, "purchase", 80, ["axe"],
        ),
        (
            {"player-1": "axe"},
            20, "purchase", 0, ["axe"],
        ),
        (
            {"player-1": "axe"},
            19, "unaffordable", 19, [],
        ),
        (
            {"player-1": "skip", "player-2": "skip"},
            100, "skip", 100, [],
        ),
        (
            {"player-1": "axe", "player-2": "water-bottle"},
            100, "tie", 100, [],
        ),
        (
            {"player-1": "axe", "player-2": "skip"},
            100, "tie", 100, [],
        ),
        ({}, 100, "tie", 100, []),
    ],
)
def test_resolution_outcomes(
    voting_game, votes, budget, expected_type,
    expected_budget, expected_ids
):
    state = voting_game["auction"]
    state["votes"] = votes
    state["budget"] = budget
    auction.socketio.start_background_task.reset_mock()

    result = auction._resolve("ABCD", voting_game, "timer")

    assert result is True
    assert state["status"] == "resolved"
    assert state["ends_at"] is None
    assert state["round_result"]["type"] == expected_type
    assert state["round_result"]["reason"] == "timer"
    assert state["budget"] == expected_budget
    assert [
        item["id"] for item in state["purchased_items"]
    ] == expected_ids
    auction.socketio.start_background_task.assert_called_once_with(
        auction._advance, "ABCD", 0
    )


def test_resolution_cannot_charge_twice(voting_game):
    state = voting_game["auction"]
    state["votes"] = {"player-1": "axe"}
    auction._resolve("ABCD", voting_game, "timer")
    budget = state["budget"]
    auction.socketio.start_background_task.reset_mock()

    result = auction._resolve("ABCD", voting_game, "timer")

    assert result is False
    assert state["budget"] == budget
    assert len(state["purchased_items"]) == 1
    auction.socketio.start_background_task.assert_not_called()


def test_broadcast_keeps_votes_anonymous(voting_game):
    voting_game["auction"]["votes"] = {"player-1": "axe"}

    auction.broadcast_auction_state("ABCD", voting_game)

    args, kwargs = auction.socketio.emit.call_args
    event, state = args
    assert event == "auction_state"
    assert kwargs["room"] == "ABCD"
    assert state["voteCount"] == 1
    assert state["playerCount"] == 2
    assert "votes" not in state
    assert "myVote" not in state


def test_personal_state_only_contains_own_vote(voting_game):
    voting_game["auction"]["votes"] = {
        "player-1": "axe",
        "player-2": "water-bottle",
    }

    auction.emit_auction_state_to_player(voting_game, "player-1")

    event, state = auction.emit.call_args.args
    assert event == "auction_state"
    assert state["myVote"] == "axe"
    assert "votes" not in state


@pytest.mark.parametrize(
    "phase, status, token, should_resolve",
    [
        ("auction", "voting", 7, True),
        ("auction", "voting", 6, False),
        ("auction", "resolved", 7, False),
        ("mission", "voting", 7, False),
    ],
)
def test_timer_only_resolves_current_active_round(
    auction_game, monkeypatch, phase, status,
    token, should_resolve
):
    auction_game["phase"] = phase
    auction_game["auction"]["status"] = status
    auction_game["auction"]["timer_token"] = 7
    resolve = Mock()
    monkeypatch.setattr(auction, "_resolve", resolve)

    auction._timer("ABCD", token)

    if should_resolve:
        resolve.assert_called_once_with(
            "ABCD", auction_game, "timer"
        )
    else:
        resolve.assert_not_called()


def test_advance_starts_next_round(voting_game):
    state = voting_game["auction"]
    state["status"] = "resolved"

    auction._advance("ABCD", 0)

    assert state["round_index"] == 1
    assert state["status"] == "voting"
    assert state["current_item_pair"] == list(
        auction.ITEM_PAIRS[1]
    )


@pytest.mark.parametrize(
    "phase, status, resolved_round",
    [
        ("mission", "resolved", 0),
        ("auction", "voting", 0),
        ("auction", "resolved", 1),
    ],
)
def test_invalid_advance_is_ignored(
    auction_game, phase, status, resolved_round
):
    auction_game["phase"] = phase
    state = auction_game["auction"]
    state["status"] = status

    auction._advance("ABCD", resolved_round)

    assert state["round_index"] == 0
    auction.socketio.start_background_task.assert_not_called()


@pytest.mark.parametrize(
    "player, all_finished, expected",
    [
        ("player-1", True, True),
        ("player-1", False, False),
        ("player-2", True, False),
        ("unknown", True, False),
    ],
)
def test_host_resolution_permissions(
    voting_game, monkeypatch, player, all_finished, expected
):
    if all_finished:
        voting_game["auction"]["finished_players"] = {
            "player-1", "player-2"
        }

    resolve = Mock()
    monkeypatch.setattr(auction, "_resolve", resolve)

    auction.resolve_auction_round(payload(player=player))

    if expected:
        resolve.assert_called_once_with(
            "ABCD", voting_game, "host"
        )
    else:
        resolve.assert_not_called()