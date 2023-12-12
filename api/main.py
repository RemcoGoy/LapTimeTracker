from fastapi import FastAPI

from .db import models
from .db.database import engine
from .routers import sessions

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sessions.router)


@app.get("/")
async def main():
    return {"message": "Hello World"}
