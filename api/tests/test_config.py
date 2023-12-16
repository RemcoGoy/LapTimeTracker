import os

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from ..db.database import Base
from ..dependencies import get_db
from ..main import app
from .seed import seed_cars, seed_games, seed_sessions, seed_tracks

load_dotenv()

client = TestClient(app)

engine = create_engine(
    os.getenv("DB_CONNECTION_STRING") + os.getenv("TEST_DB_NAME"),
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    seed_games(db)
    seed_tracks(db)
    seed_cars(db)
    seed_sessions(db)

    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)
