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


# endregion
