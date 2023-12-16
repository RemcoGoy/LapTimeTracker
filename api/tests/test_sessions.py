from datetime import datetime

from ..db import crud, schemas
from .seed.cars import seeded_cars
from .seed.sessions import seeded_sessions
from .seed.tracks import seeded_tracks
from .test_config import client, session


def test_create_session(client, session):
    session_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    response = client.post(
        "/sessions/",
        json={
            "start_time": session_time,
            "car_id": str(seeded_cars[0]["id"]),
            "track_id": str(seeded_tracks[0]["id"]),
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["start_time"] == session_time
    assert "id" in data
    session_id = data["id"]

    session_obj = crud.get_session(session, session_id)
    assert session_id == str(session_obj.id)

    deleted = crud.delete_session(session, session_id)
    assert deleted == 1


def test_get_session(client):
    session_obj = seeded_sessions[0]

    response = client.get(f"/sessions/{session_obj['id']}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["start_time"] == session_obj["start_time"]
    assert data["id"] == str(session_obj["id"])


def test_get_sessions(client):
    n_sessions = len(seeded_sessions)

    response = client.get("/sessions")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == n_sessions


def test_delete_session(client, session):
    session_obj = crud.create_session(
        session,
        schemas.SessionCreate(
            start_time=datetime.now(), car_id=seeded_cars[0]["id"], track_id=seeded_tracks[0]["id"]
        ),
    )

    n_sessions_before = len(crud.get_sessions(session))

    response = client.delete(f"/sessions/{session_obj.id}")
    assert response.status_code == 200
    assert response.json() == 1

    n_sessions_after = len(crud.get_sessions(session))

    assert n_sessions_before == n_sessions_after + 1


def test_update_session(client, session):
    new_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    session_obj = crud.create_session(
        session,
        schemas.SessionCreate(
            start_time=datetime.now(), car_id=seeded_cars[0]["id"], track_id=seeded_tracks[0]["id"]
        ),
    )

    response = client.patch(f"/sessions/{session_obj.id}", json={"start_time": new_time})
    assert response.status_code == 200, response.text
    data = response.json()

    session_obj = crud.get_session(session, session_obj.id)

    assert data["start_time"] == new_time
    assert data["id"] == str(session_obj.id)
    assert session_obj.start_time.strftime("%Y-%m-%dT%H:%M:%S") == new_time
