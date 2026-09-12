from types import SimpleNamespace
from unittest.mock import Mock

import flask
import pytest

from app.sockets.handlers import auction, lobby, mission
from app.sockets.sessions import sessions


@pytest.fixture
def lobby_io(monkeypatch):
    """Replace socket operations and cross-module calls."""
    mocks = SimpleNamespace(
        request=SimpleNamespace(sid="socket-1"),
        emit=Mock(),
        broadcast=Mock(),
        join_room=Mock(),
        background=Mock(),
        sleep=Mock(),
        initialise_auction=Mock(),
        auction_state=Mock(),
        mission_state=Mock(),
        build_results=Mock(),
    )

    # Lobby imports request inside its handlers.
    monkeypatch.setattr(flask, "request", mocks.request)
    monkeypatch.setattr(lobby, "emit", mocks.emit)
    monkeypatch.setattr(lobby, "join_room", mocks.join_room)
    monkeypatch.setattr(lobby.socketio, "emit", mocks.broadcast)
    monkeypatch.setattr(
        lobby.socketio, "start_background_task", mocks.background
    )
    monkeypatch.setattr(lobby.socketio, "sleep", mocks.sleep)
    monkeypatch.setattr(
        auction, "initialise_auction", mocks.initialise_auction
    )
    monkeypatch.setattr(
        auction, "emit_auction_state_to_player", mocks.auction_state
    )
    monkeypatch.setattr(
        mission, "emit_mission_state_to_player", mocks.mission_state
    )
    monkeypatch.setattr(
        lobby, "build_result_state", mocks.build_results
    )

    return mocks


@pytest.fixture
def lobby_game(sample_session, lobby_io):
    sample_session["players"]["player-1"]["socket_id"] = "socket-1"
    sample_session["players"]["player-2"]["socket_id"] = "socket-2"
    return sample_session


def join_payload(**changes):
    data = {
        "sessionCode": "ABCD",
        "name": "New Player",
        "isHost": False,
    }
    data.update(changes)
    return data


def action_payload(player="player-1", **changes):
    data = {"sessionCode": "ABCD", "playerId": player}
    data.update(changes)
    return data


def joined_data(lobby_io):
    """Get the private 'joined' response."""
    responses = [
        call.args[1]
        for call in lobby_io.emit.call_args_list
        if call.args[0] == "joined"
    ]
    assert len(responses) == 1
    return responses[0]


def test_host_creates_session(lobby_io):
    lobby.handle_join_session(
        join_payload(isHost=True, name="Abbey")
    )

    session = sessions["ABCD"]
    data = joined_data(lobby_io)
    player_id = data["playerId"]

    assert session["host_id"] == player_id
    assert session["players"][player_id] == {
        "name": "Abbey",
        "ready": False,
        "connected": True,
        "socket_id": "socket-1",
    }
    assert data["isHost"] is True
    assert data["phase"] == "lobby"
    lobby_io.join_room.assert_called_once_with("ABCD")


def test_join_unknown_session_is_rejected(lobby_io):
    lobby.handle_join_session(join_payload())

    assert "ABCD" not in sessions
    lobby_io.emit.assert_called_once_with("invalid_session")
    lobby_io.join_room.assert_not_called()


def test_guest_joins_without_replacing_host(lobby_game, lobby_io):
    lobby.handle_join_session(join_payload(name="Taylor"))

    data = joined_data(lobby_io)
    assert len(lobby_game["players"]) == 3
    assert lobby_game["players"][data["playerId"]]["name"] == "Taylor"
    assert lobby_game["host_id"] == "player-1"
    assert data["isHost"] is False


def test_blank_name_gets_default(lobby_game, lobby_io):
    lobby.handle_join_session(join_payload(name=""))

    player_id = joined_data(lobby_io)["playerId"]
    assert lobby_game["players"][player_id]["name"] == "Player 3"


def test_host_flag_does_not_replace_existing_host(lobby_game, lobby_io):
    lobby.handle_join_session(join_payload(isHost=True))

    assert lobby_game["host_id"] == "player-1"
    assert joined_data(lobby_io)["isHost"] is False


def test_reconnect_preserves_player_and_updates_socket(
    lobby_game, lobby_io
):
    player = lobby_game["players"]["player-1"]
    player["connected"] = False
    player["ready"] = True
    lobby_io.request.sid = "replacement-socket"

    lobby.handle_join_session(
        join_payload(playerId="player-1", name="Changed Name")
    )

    assert len(lobby_game["players"]) == 2
    assert player["name"] == "Abbey"
    assert player["ready"] is True
    assert player["connected"] is True
    assert player["socket_id"] == "replacement-socket"
    assert joined_data(lobby_io)["playerId"] == "player-1"


@pytest.mark.parametrize("phase", ["auction", "mission"])
def test_reconnect_restores_phase_state(lobby_game, lobby_io, phase):
    lobby_game["phase"] = phase
    lobby_game["auction"] = {"status": "voting"}
    lobby_game["auction_start_time"] = 1234

    if phase == "mission":
        lobby_game["mission"] = {"status": "active"}

    lobby.handle_join_session(join_payload(playerId="player-1"))

    lobby_io.auction_state.assert_called_once_with(
        lobby_game, "player-1"
    )

    if phase == "mission":
        lobby_io.mission_state.assert_called_once_with(lobby_game)
    else:
        assert joined_data(lobby_io)["auctionStartTime"] == 1234
        lobby_io.mission_state.assert_not_called()


@pytest.mark.parametrize("available", [True, False])
def test_results_arrival_sends_results_or_error(
    lobby_game, lobby_io, available
):
    lobby_game["phase"] = "result_page"
    result = {"finalScore": 90} if available else None
    lobby_io.build_results.return_value = result

    lobby.handle_join_session(join_payload(playerId="player-1"))

    lobby_io.build_results.assert_called_once_with(lobby_game)

    if available:
        lobby_io.emit.assert_any_call("result_state", result)
    else:
        lobby_io.emit.assert_any_call(
            "result_error",
            {"message": "Results are not available for this game yet."},
        )


@pytest.mark.parametrize("ready", [True, False])
def test_player_can_change_ready_status(lobby_game, lobby_io, ready):
    lobby_game["players"]["player-1"]["ready"] = not ready

    lobby.handle_player_ready(action_payload(ready=ready))

    assert lobby_game["players"]["player-1"]["ready"] is ready
    lobby_io.broadcast.assert_called_once()


def test_unknown_player_cannot_ready_up(lobby_game, lobby_io):
    lobby.handle_player_ready(
        action_payload(player="unknown", ready=True)
    )

    assert all(
        not player["ready"]
        for player in lobby_game["players"].values()
    )
    lobby_io.broadcast.assert_not_called()


def test_ready_players_do_not_automatically_start_game(
    lobby_game, lobby_io
):
    for player in ("player-1", "player-2"):
        lobby.handle_player_ready(
            action_payload(player=player, ready=True)
        )

    assert lobby_game["phase"] == "lobby"
    lobby_io.initialise_auction.assert_not_called()


def test_host_starts_when_everyone_ready(lobby_game, lobby_io):
    for player in lobby_game["players"].values():
        player["ready"] = True

    lobby.handle_start_game(action_payload())

    assert lobby_game["phase"] == "start_game"
    lobby_io.initialise_auction.assert_called_once_with(lobby_game)
    lobby_io.emit.assert_called_once_with(
        "game_started", {"phase": "start_game"}, room="ABCD"
    )


@pytest.mark.parametrize(
    "player, everyone_ready",
    [
        ("player-2", True),
        ("unknown", True),
        ("player-1", False),
    ],
)
def test_game_start_requires_host_and_readiness(
    lobby_game, lobby_io, player, everyone_ready
):
    for entry in lobby_game["players"].values():
        entry["ready"] = everyone_ready

    lobby.handle_start_game(action_payload(player=player))

    assert lobby_game["phase"] == "lobby"
    lobby_io.initialise_auction.assert_not_called()
    lobby_io.emit.assert_not_called()


def test_empty_lobby_cannot_start(lobby_game, lobby_io):
    lobby_game["players"].clear()

    lobby.handle_start_game(action_payload())

    assert lobby_game["phase"] == "lobby"
    lobby_io.initialise_auction.assert_not_called()


def test_host_starts_auction_with_shared_timestamp(
    lobby_game, lobby_io, monkeypatch
):
    lobby_game["phase"] = "start_game"
    monkeypatch.setattr(lobby.time, "time", lambda: 1234)

    lobby.handle_start_auction(action_payload())

    assert lobby_game["phase"] == "auction"
    assert lobby_game["auction_start_time"] == 1234
    lobby_io.emit.assert_called_once_with(
        "auction_started",
        {"phase": "auction", "auctionStartTime": 1234},
        room="ABCD",
    )


@pytest.mark.parametrize(
    "player, phase",
    [
        ("player-2", "start_game"),
        ("unknown", "start_game"),
        ("player-1", "lobby"),
        ("player-1", "auction"),
        ("player-1", "mission"),
    ],
)
def test_invalid_auction_start_is_ignored(
    lobby_game, lobby_io, player, phase
):
    lobby_game["phase"] = phase

    lobby.handle_start_auction(action_payload(player=player))

    assert lobby_game["phase"] == phase
    assert "auction_start_time" not in lobby_game
    lobby_io.emit.assert_not_called()


def test_auction_start_does_not_create_unknown_session(lobby_io):
    lobby.handle_start_auction(action_payload())

    assert "ABCD" not in sessions
    lobby_io.emit.assert_not_called()


@pytest.mark.parametrize("player", ["player-1", "player-2"])
def test_disconnect_marks_player_and_schedules_host_check(
    lobby_game, lobby_io, player
):
    lobby_io.request.sid = lobby_game["players"][player]["socket_id"]

    lobby.handle_disconnect()

    assert lobby_game["players"][player]["connected"] is False
    assert lobby_game["players"][player]["socket_id"] is None
    lobby_io.broadcast.assert_called_once()

    if player == "player-1":
        lobby_io.background.assert_called_once_with(
            lobby.reassign_host_after_disconnect, "ABCD", player
        )
    else:
        lobby_io.background.assert_not_called()


def test_unknown_socket_disconnect_is_ignored(lobby_game, lobby_io):
    lobby_io.request.sid = "unknown-socket"

    lobby.handle_disconnect()

    assert all(
        player["connected"]
        for player in lobby_game["players"].values()
    )
    lobby_io.broadcast.assert_not_called()
    lobby_io.background.assert_not_called()


def test_disconnected_host_is_reassigned(lobby_game, lobby_io):
    lobby_game["players"]["player-1"]["connected"] = False

    lobby.reassign_host_after_disconnect("ABCD", "player-1")

    lobby_io.sleep.assert_called_once_with(30)
    assert lobby_game["host_id"] == "player-2"
    lobby_io.broadcast.assert_any_call(
        "host_changed", {"hostId": "player-2"}, room="ABCD"
    )


@pytest.mark.parametrize("reason", ["reconnected", "changed", "deleted"])
def test_host_reassignment_cancels_when_no_longer_needed(
    lobby_game, lobby_io, reason
):
    if reason == "changed":
        lobby_game["host_id"] = "player-2"
    elif reason == "deleted":
        del sessions["ABCD"]
    # For "reconnected", player-1 is already connected.

    lobby.reassign_host_after_disconnect("ABCD", "player-1")

    lobby_io.broadcast.assert_not_called()


def test_no_host_change_event_when_everyone_disconnected(
    lobby_game, lobby_io
):
    for player in lobby_game["players"].values():
        player["connected"] = False

    lobby.reassign_host_after_disconnect("ABCD", "player-1")

    events = [
        call.args[0] for call in lobby_io.broadcast.call_args_list
    ]
    assert "host_changed" not in events
    assert "lobby_state" in events


def test_lobby_broadcast_contains_public_player_data(
    lobby_game, lobby_io
):
    lobby.broadcast_lobby_state("ABCD", lobby_game)

    lobby_io.broadcast.assert_called_once_with(
        "lobby_state",
        {
            "players": [
                {
                    "id": "player-1",
                    "name": "Abbey",
                    "ready": False,
                    "connected": True,
                    "isHost": True,
                },
                {
                    "id": "player-2",
                    "name": "Alex",
                    "ready": False,
                    "connected": True,
                    "isHost": False,
                },
            ],
            "phase": "lobby",
        },
        room="ABCD",
    )