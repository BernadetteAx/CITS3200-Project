from app.sockets.sessions import (
    sessions,
    get_or_create_session,
    get_session,
    change_host,
)


def test_create_session_has_correct_defaults():
    session = get_or_create_session("ABCD")

    assert session == {
        "phase": "lobby",
        "host_id": None,
        "players": {},
    }
    assert sessions["ABCD"] is session


def test_existing_session_is_not_reset(sample_session):
    sample_session["phase"] = "auction"
    sample_session["players"]["player-1"]["ready"] = True

    result = get_or_create_session("ABCD")

    assert result is sample_session
    assert result["phase"] == "auction"
    assert result["players"]["player-1"]["ready"] is True
    assert len(result["players"]) == 2


def test_different_sessions_have_independent_players():
    first = get_or_create_session("ABCD")
    second = get_or_create_session("WXYZ")

    first["players"]["player-1"] = {
        "name": "Abbey",
        "ready": False,
        "connected": True,
    }

    assert second["players"] == {}


def test_get_existing_session(sample_session):
    assert get_session("ABCD") is sample_session


def test_get_unknown_session_does_not_create_it():
    assert get_session("MISSING") is None
    assert "MISSING" not in sessions


def test_change_host_selects_first_connected_player(sample_session):
    sample_session["host_id"] = "player-2"

    result = change_host(sample_session)

    assert result == "player-1"
    assert sample_session["host_id"] == "player-1"


def test_change_host_skips_disconnected_players(sample_session):
    sample_session["players"]["player-1"]["connected"] = False

    result = change_host(sample_session)

    assert result == "player-2"
    assert sample_session["host_id"] == "player-2"


def test_change_host_returns_none_when_everyone_disconnected(
    sample_session,
):
    for player in sample_session["players"].values():
        player["connected"] = False

    assert change_host(sample_session) is None


def test_change_host_returns_none_when_no_players():
    session = get_or_create_session("ABCD")

    assert change_host(session) is None
    assert session["host_id"] is None