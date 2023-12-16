from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import models
from .db.database import engine
from .routers import cars, games, laps, sessions, tracks

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(games.router)
app.include_router(tracks.router)
app.include_router(cars.router)
app.include_router(sessions.router)
app.include_router(laps.router)


@app.get("/")
async def main():
    return {"message": "Hello World"}
