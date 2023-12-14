import os

from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from ..db.database import Base
from ..dependencies import get_db
from ..main import app

load_dotenv()

client = TestClient(app)

engine = create_engine(
    os.getenv("DB_CONNECTION_STRING") + os.getenv("TEST_DB_NAME"),
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_game():
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
