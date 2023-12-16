import pytest

from ..db import crud, schemas
from .seed.games import seeded_games
from .test_config import client, session


def test_create_game(client, session):
    game_name = "TestGame1"

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

    resposne = client.get(f"/games/{game['id']}")
    assert resposne.status_code == 200
    data = resposne.json()
    assert data["name"] == game["name"]
    assert data["id"] == str(game["id"])
