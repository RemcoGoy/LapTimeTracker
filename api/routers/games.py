import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import crud, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/games", tags=["games"])


@router.get("/", response_model=List[schemas.Game])
async def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_games(db, skip=skip, limit=limit)


@router.get("/{game_id}", response_model=schemas.Game)
async def read_game(game_id: uuid.UUID, db: Session = Depends(get_db)):
    db_game = crud.get_game(db, game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")

    return db_game


@router.post("/", response_model=schemas.Game)
async def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    print("HERE")
    return crud.create_game(db, game)


@router.patch("/{game_id}", response_model=schemas.Game)
async def update_game(
    game_id: uuid.UUID, update: schemas.GameUpdate, db: Session = Depends(get_db)
):
    db_game = crud.update_game(db, game_id, update)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")

    return db_game


@router.delete("/{game_id}", response_model=int, response_description="Number of deleted rows")
async def delete_game(game_id: uuid.UUID, db: Session = Depends(get_db)):
    rows_deleted = crud.delete_game(db, game_id)
    if rows_deleted == 0:
        raise HTTPException(status_code=404, detail="Game not found")

    return rows_deleted


@router.post("/{game_id}/car", response_model=schemas.Car)
async def create_car_for_game(
    game_id: uuid.UUID, car: schemas.CarCreate, db: Session = Depends(get_db)
):
    db_car = crud.create_car(db, car, game_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Game not found")

    return db_car


@router.post("/{game_id}/track", response_model=schemas.Track)
async def create_track_for_game(
    game_id: uuid.UUID, track: schemas.TrackCreate, db: Session = Depends(get_db)
):
    db_track = crud.create_track(db, track, game_id)
    if db_track is None:
        raise HTTPException(status_code=404, detail="Game not found")

    return db_track
