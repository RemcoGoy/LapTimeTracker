import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import crud, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.get("/")
async def read_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_sessions(db, skip=skip, limit=limit)


@router.get("/{session_id}")
async def read_session(session_id: uuid.UUID, db: Session = Depends(get_db)):
    db_session = crud.get_session(db, session_id)
    if db_session is None:
        raise HTTPException(status_code=404, detail="Session not found")


@router.post("/{session_id}/lap", response_model=schemas.Lap)
async def create_lap_for_session(
    session_id: uuid.UUID, lap: schemas.LapCreate, db: Session = Depends(get_db)
):
    return crud.create_lap(db, lap, session_id)
