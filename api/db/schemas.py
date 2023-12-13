import uuid

from pydantic import BaseModel


class IdBase:
    id: uuid.UUID


class LapBase(BaseModel):
    time: float


class LapCreate(LapBase):
    pass


class Lap(IdBase, LapBase):
    class Config:
        orm_mode = True


class SessionBase(BaseModel):
    pass


class SessionCreate(SessionBase):
    pass


class Session(IdBase, SessionBase):
    track_id: uuid.UUID
    car_id: uuid.UUID
    laps: list[Lap]

    class Config:
        orm_mode = True


class TrackBase(BaseModel):
    name: str
    country: str


class TrackCreate(TrackBase):
    pass


class Track(IdBase, TrackBase):
    game_id: uuid.UUID

    class Config:
        orm_mode = True


class GameBase(BaseModel):
    name: str


class GameCreate(GameBase):
    pass


class Game(IdBase, GameBase):
    tracks: list[Track]

    class Config:
        orm_mode = True


class CarBase(BaseModel):
    make: str
    model: str
    car_class: str


class CarCreate(CarBase):
    pass


class Car(IdBase, CarBase):
    class Config:
        orm_mode = True
