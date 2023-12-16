from ..db import crud, schemas
from .seed.laps import seeded_laps
from .seed.sessions import seeded_sessions
from .test_config import client, session


def test_create_lap(client, session):
    lap_time = 99

    response = client.post(
        f"/sessions/{seeded_sessions[0]['id']}/lap",
        json={"time": lap_time},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["time"] == lap_time
    assert "id" in data
    lap_id = data["id"]

    lap = crud.get_lap(session, lap_id)
    assert lap_id == str(lap.id)

    deleted = crud.delete_lap(session, lap_id)
    assert deleted == 1


def test_get_lap(client):
    lap = seeded_laps[0]

    response = client.get(f"/laps/{lap['id']}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["time"] == lap["time"]
    assert data["id"] == str(lap["id"])


def test_get_laps(client):
    n_laps = len(seeded_laps)

    response = client.get("/laps")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == n_laps


def test_delete_lap(client, session):
    lap = crud.create_lap(session, schemas.LapCreate(time=150), session_id=seeded_sessions[0]["id"])

    n_laps_before = len(crud.get_laps(session))

    response = client.delete(f"/laps/{lap.id}")
    assert response.status_code == 200
    assert response.json() == 1

    n_laps_after = len(crud.get_laps(session))

    assert n_laps_before == n_laps_after + 1


def test_update_lap(client, session):
    new_time = 20

    lap = crud.create_lap(session, schemas.LapCreate(time=100), session_id=seeded_sessions[0]["id"])

    response = client.patch(f"/laps/{lap.id}", json={"time": new_time})
    assert response.status_code == 200, response.text
    data = response.json()

    lap = crud.get_lap(session, lap.id)

    assert data["time"] == new_time
    assert data["id"] == str(lap.id)
    assert lap.time == new_time
