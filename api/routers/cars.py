import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import crud, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/cars", tags=["cars"])


@router.get("/", response_model=List[schemas.Car])
async def read_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_cars(db, skip=skip, limit=limit)


@router.get("/{car_id}", response_model=schemas.Car)
async def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")

    return db_car


@router.patch("/{car_id}", response_model=schemas.Car)
async def update_car(car_id: uuid.UUID, update: schemas.CarUpdate, db: Session = Depends(get_db)):
    db_car = crud.update_car(db, car_id, update)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")

    return db_car


@router.delete("/{car_id}", response_model=int, response_description="Number of deleted rows")
async def delete_car(car_id: uuid.UUID, db: Session = Depends(get_db)):
    rows_deleted = crud.delete_car(db, car_id)
    if rows_deleted == 0:
        raise HTTPException(status_code=404, detail="Car not found")

    return rows_deleted
