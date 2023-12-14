import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import crud, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/laps", tags=["laps"])


@router.get("/", response_model=List[schemas.Lap])
async def read_laps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_laps(db, skip=skip, limit=limit)


@router.get("/{lap_id}", response_model=schemas.Lap)
async def read_laps(lap_id: uuid.UUID, db: Session = Depends(get_db)):
    db_lap = crud.get_lap(db, lap_id)
    if db_lap is None:
        raise HTTPException(status_code=404, detail="Lap not found")

    return db_lap


@router.patch("/{lap_id}", response_model=schemas.Lap)
async def update_lap(lap_id: uuid.UUID, update: schemas.LapUpdate, db: Session = Depends(get_db)):
    db_lap = crud.update_lap(db, lap_id, update)
    if db_lap is None:
        raise HTTPException(status_code=404, detail="Lap not found")

    return db_lap


@router.delete("/{lap_id}", response_model=int, response_description="Number of deleted rows")
async def delete_lap(lap_id: uuid.UUID, db: Session = Depends(get_db)):
    rows_deleted = crud.delete_lap(db, lap_id)
    if rows_deleted == 0:
        raise HTTPException(status_code=404, detail="Lap not found")

    return rows_deleted
