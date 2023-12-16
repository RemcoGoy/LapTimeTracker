import uuid

from ...db.models import Game

seeded_games = [{"id": uuid.UUID("893ace05-dbc5-47d1-8528-122b59ef2c4f"), "name": "TestGame"}]


def seed_games(db_session):
    for game in seeded_games:
        db_game = Game(id=game["id"], name=game["name"])
        db_session.add(db_game)
    db_session.commit()
