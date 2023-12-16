import uuid

from ...db.models import Car
from .games import seeded_games

seeded_cars = [
    {
        "id": uuid.uuid4(),
        "make": "McLaren",
        "model": "720s EVO",
        "car_class": "GT3",
        "game_id": seeded_games[0]["id"],
    },
    {
        "id": uuid.uuid4(),
        "make": "Ferrari",
        "model": "296",
        "car_class": "GT3",
        "game_id": seeded_games[1]["id"],
    },
]


def seed_cars(db_session):
    for car in seeded_cars:
        db_car = Car(
            id=car["id"],
            make=car["make"],
            model=car["model"],
            car_class=car["car_class"],
            game_id=car["game_id"],
        )
        db_session.add(db_car)
    db_session.commit()
