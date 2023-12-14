import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import crud, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/laps", tags=["laps"])


@router.get("/")
async def read_laps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_laps(db, skip=skip, limit=limit)
