import uuid

from sqlalchemy.orm import Session

from . import models, schemas


def get_session(db: Session, session_id: uuid.UUID):
    return db.query(models.Session).filter(models.Session.id == session_id).first()


def get_sessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Session).offset(skip).limit(limit).all()


def create_session(db: Session, session: schemas.SessionCreate):
    db_session = models.Session(laps=session.laps)
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session
