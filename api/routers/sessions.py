from fastapi import APIRouter

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.get("/")
async def get_sessions():
    return []
