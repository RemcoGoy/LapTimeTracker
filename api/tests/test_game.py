import pytest

from ..db import crud
from .test_config import client


class TestGame:
    def test_create_game(self):
        response = client.post("/games/", json={"name": "TestGame"})
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["name"] == "TestGame"
        assert "id" in data
        game_id = data["id"]

        response = client.get(f"/games/{game_id}")
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["name"] == "TestGame"
        assert data["id"] == game_id
