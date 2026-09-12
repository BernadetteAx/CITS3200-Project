import pytest

# import from where our sessions.py lives
from app.sockets.sessions import sessions


@pytest.fixture(autouse=True)
def reset_sessions():
    """Give every test a clean session store."""
    sessions.clear()

    yield

    sessions.clear()


@pytest.fixture
def sample_session():
    """Provide an example game with a host and another player."""
    session = {
        "phase": "lobby",
        "host_id": "player-1",
        "players": {
            "player-1": {
                "name": "Abbey",
                "ready": False,
                "connected": True,
            },
            "player-2": {
                "name": "Alex",
                "ready": False,
                "connected": True,
            },
        },
    }

    sessions["ABCD"] = session
    return session