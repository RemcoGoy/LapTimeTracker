import uuid

from sqlalchemy.orm import Session

from . import models, schemas


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


def get_lap(db: Session, lap_id: uuid.UUID):
    return db.query(models.Lap).filter(models.Lap.id == lap_id).first()


def get_laps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lap).offset(skip).limit(limit).all()


def create_lap(db: Session, lap: schemas.LapCreate, session_id: uuid.UUID):
    db_lap = models.Lap(time=lap.time, session_id=session_id)
    db.add(db_lap)
    db.commit()
    db.refresh(db_lap)
    return db_lap
