from ..db import crud, schemas
from .seed.games import seeded_games
from .seed.tracks import seeded_tracks
from .test_config import client, session


def test_create_track(client, session):
    track_name = "TestTrack2"
    track_country = "Belgium"

    response = client.post(
        f"/games/{seeded_games[0]['id']}/track", json={"name": track_name, "country": track_country}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == track_name
    assert "id" in data
    track_id = data["id"]

    track = crud.get_track(session, track_id)
    assert track_id == str(track.id)

    deleted = crud.delete_track(session, track_id)
    assert deleted == 1


def test_get_track(client):
    track = seeded_tracks[0]

    response = client.get(f"/tracks/{track['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == track["name"]
    assert data["country"] == track["country"]
    assert data["id"] == str(track["id"])


def test_get_tracks(client):
    n_tracks = len(seeded_tracks)

    response = client.get("/tracks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == n_tracks


def test_delete_track(client, session):
    track = crud.create_track(
        session, schemas.TrackCreate(name="AddTrack", country="UK"), game_id=seeded_games[0]["id"]
    )

    n_tracks_before = len(crud.get_tracks(session))

    response = client.delete(f"/tracks/{track.id}")
    assert response.status_code == 200
    assert response.json() == 1

    n_tracks_after = len(crud.get_tracks(session))

    assert n_tracks_before == n_tracks_after + 1


def test_update_track(client, session):
    new_name = "UpdatedTrack"
    track = crud.create_track(
        session,
        schemas.TrackCreate(name="AddTrack", country="Brazil"),
        game_id=seeded_games[0]["id"],
    )

    response = client.patch(f"/tracks/{track.id}", json={"name": new_name})
    assert response.status_code == 200, response.text
    data = response.json()

    track = crud.get_track(session, track.id)

    assert data["name"] == new_name
    assert data["country"] == "Brazil"
    assert data["id"] == str(track.id)
    assert track.name == new_name
