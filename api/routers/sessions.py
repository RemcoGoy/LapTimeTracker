from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import crud
from ..dependencies import get_db

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.get("/")
async def read_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_sessions(db, skip=skip, limit=limit)
