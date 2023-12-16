import uuid

from ...db.models import Game

seeded_games = [{"id": uuid.uuid4(), "name": "TestGame"}, {"id": uuid.uuid4(), "name": "TestGame1"}]


def seed_games(db_session):
    for game in seeded_games:
        db_game = Game(id=game["id"], name=game["name"])
        db_session.add(db_game)
    db_session.commit()
