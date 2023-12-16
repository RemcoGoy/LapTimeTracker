import pytest

from ..db import crud, schemas
from .seed.games import seeded_games
from .test_config import client, session


def test_create_game(client, session):
    game_name = "TestGame2"

    response = client.post("/games/", json={"name": game_name})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == game_name
    assert "id" in data
    game_id = data["id"]

    game = crud.get_game(session, game_id)
    assert game_id == str(game.id)

    deleted = crud.delete_game(session, game_id)
    assert deleted == 1


def test_get_game(client):
    game = seeded_games[0]

    response = client.get(f"/games/{game['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == game["name"]
    assert data["id"] == str(game["id"])


def test_get_games(client):
    n_games = len(seeded_games)

    response = client.get("/games")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == n_games


def test_delete_game(client, session):
    game = crud.create_game(session, schemas.GameCreate(name="AddGame"))

    n_games_before = len(crud.get_games(session))

    response = client.delete(f"/games/{game.id}")
    assert response.status_code == 200
    assert response.json() == 1

    n_games_after = len(crud.get_games(session))

    assert n_games_before == n_games_after + 1
