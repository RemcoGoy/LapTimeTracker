import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas

# region SESSION


def get_session(db: Session, session_id: uuid.UUID):
    return db.query(models.Session).filter(models.Session.id == session_id).first()


def get_sessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Session).offset(skip).limit(limit).all()


def create_session(db: Session, session: schemas.SessionCreate):
    db_session = models.Session()
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session


def update_session(db: Session, session_id: uuid.UUID, update: schemas.SessionUpdate):
    db_session = db.get(models.Session, session_id)
    if db_session is None:
        return db_session

    session_data = update.model_dump(exclude_unset=True)
    for key, value in session_data.items():
        setattr(db_session, key, value)

    db.add(db_session)
    db.commit()
    db.refresh(db_session)

    return db_session


def delete_session(db: Session, session_id: uuid.UUID):
    result = db.query(models.Session).filter(models.Session.id == session_id).delete()
    db.commit()
    return result


# endregion

# region LAP


def get_lap(db: Session, lap_id: uuid.UUID):
    return db.query(models.Lap).filter(models.Lap.id == lap_id).first()


def get_laps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lap).offset(skip).limit(limit).all()


def create_lap(db: Session, lap: schemas.LapCreate, session_id: uuid.UUID):
    db_session = db.get(models.Session, session_id)
    if db_session is None:
        return None

    db_lap = models.Lap(time=lap.time, session_id=session_id)
    db.add(db_lap)
    db.commit()
    db.refresh(db_lap)

    return db_lap


def update_lap(db: Session, lap_id: uuid.UUID, update: schemas.LapUpdate):
    db_lap = db.get(models.Lap, lap_id)
    if db_lap is None:
        return db_lap

    lap_data = update.model_dump(exclude_unset=True)
    for key, value in lap_data.items():
        setattr(db_lap, key, value)

    db.add(db_lap)
    db.commit()
    db.refresh(db_lap)

    return db_lap


def delete_lap(db: Session, lap_id: uuid.UUID):
    result = db.query(models.Lap).filter(models.Lap.id == lap_id).delete()
    db.commit()
    return result


# endregion

# region GAME


def get_game(db: Session, game_id: uuid.UUID):
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()


def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(name=game.name)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def update_game(db: Session, game_id: uuid.UUID, update: schemas.GameUpdate):
    db_game = db.get(models.Game, game_id)
    if db_game is None:
        return db_game

    game_data = update.model_dump(exclude_unset=True)
    for key, value in game_data.items():
        setattr(db_game, key, value)

    db.add(db_game)
    db.commit()
    db.refresh(db_game)

    return db_game


def delete_game(db: Session, game_id: uuid.UUID):
    result = db.query(models.Game).filter(models.Game.id == game_id).delete()
    db.commit()
    return result


# endregion

# region TRACK


def get_track(db: Session, track_id: uuid.UUID):
    return db.query(models.Track).filter(models.Track.id == track_id).first()


def get_tracks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Track).offset(skip).limit(limit).all()


def update_track(db: Session, track_id: uuid.UUID, update: schemas.TrackUpdate):
    db_track = db.get(models.Track, track_id)
    if db_track is None:
        return db_track

    track_data = update.model_dump(exclude_unset=True)
    for key, value in track_data.items():
        setattr(db_track, key, value)

    db.add(db_track)
    db.commit()
    db.refresh(db_track)

    return db_track


def delete_track(db: Session, track_id: uuid.UUID):
    result = db.query(models.Track).filter(models.Track.id == track_id).delete()
    db.commit()
    return result


# endregion

# region CAR


def get_car(db: Session, car_id: uuid.UUID):
    return db.query(models.Car).filter(models.Car.id == car_id).first()


def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Car).offset(skip).limit(limit).all()


def update_car(db: Session, car_id: uuid.UUID, update: schemas.CarUpdate):
    db_car = db.get(models.Car, car_id)
    if db_car is None:
        return db_car

    car_data = update.model_dump(exclude_unset=True)
    for key, value in car_data.items():
        setattr(db_car, key, value)

    db.add(db_car)
    db.commit()
    db.refresh(db_car)

    return db_car


def delete_car(db: Session, car_id: uuid.UUID):
    result = db.query(models.Car).filter(models.Car.id == car_id).delete()
    db.commit()
    return result


# endregion
