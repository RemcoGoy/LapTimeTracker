import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import crud, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/tracks", tags=["tracks"])


@router.get("/", response_model=List[schemas.Track])
async def read_tracks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tracks(db, skip=skip, limit=limit)


@router.get("/{track_id}", response_model=schemas.Track)
async def read_track(track_id: uuid.UUID, db: Session = Depends(get_db)):
    db_track = crud.get_track(db, track_id)
    if db_track is None:
        raise HTTPException(status_code=404, detail="Track not found")

    return db_track


@router.patch("/{track_id}", response_model=schemas.Track)
async def update_track(
    track_id: uuid.UUID, update: schemas.TrackUpdate, db: Session = Depends(get_db)
):
    db_track = crud.update_track(db, track_id, update)
    if db_track is None:
        raise HTTPException(status_code=404, detail="Track not found")

    return db_track


@router.delete("/{track_id}", response_model=int, response_description="Number of deleted rows")
async def delete_track(track_id: uuid.UUID, db: Session = Depends(get_db)):
    rows_deleted = crud.delete_track(db, track_id)
    if rows_deleted == 0:
        raise HTTPException(status_code=404, detail="Track not found")

    return rows_deleted
