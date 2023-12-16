import uuid
from datetime import datetime

from ...db.models import Session
from .cars import seeded_cars
from .tracks import seeded_tracks

seeded_sessions = [
    {
        "id": uuid.uuid4(),
        "start_time": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "track_id": seeded_tracks[0]["id"],
        "car_id": seeded_cars[0]["id"],
    },
    {
        "id": uuid.uuid4(),
        "start_time": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "track_id": seeded_tracks[1]["id"],
        "car_id": seeded_cars[1]["id"],
    },
]


def seed_sessions(db_session):
    for session in seeded_sessions:
        db_sesh = Session(
            id=session["id"],
            start_time=session["start_time"],
            track_id=session["track_id"],
            car_id=session["car_id"],
        )
        db_session.add(db_sesh)
    db_session.commit()
