import uuid

from ...db.models import Lap
from .sessions import seeded_sessions

seeded_laps = [
    {"id": uuid.uuid4(), "time": 100, "session_id": seeded_sessions[0]["id"]},
    {"id": uuid.uuid4(), "time": 120, "session_id": seeded_sessions[1]["id"]},
]


def seed_laps(db_session):
    for lap in seeded_laps:
        db_lap = Lap(id=lap["id"], time=lap["time"], session_id=lap["session_id"])
        db_session.add(db_lap)
    db_session.commit()
