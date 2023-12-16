import uuid

from ...db.models import Track
from .games import seeded_games

seeded_tracks = [
    {
        "id": uuid.uuid4(),
        "name": "TestTrack",
        "country": "Germany",
        "game_id": seeded_games[0]["id"],
    },
    {
        "id": uuid.uuid4(),
        "name": "TestTrack1",
        "country": "Austria",
        "game_id": seeded_games[1]["id"],
    },
]


def seed_tracks(db_session):
    for track in seeded_tracks:
        db_track = Track(
            id=track["id"], name=track["name"], country=track["country"], game_id=track["game_id"]
        )
        db_session.add(db_track)
    db_session.commit()
