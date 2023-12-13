import uuid

from pydantic import BaseModel


class IdBase:
    id: uuid.UUID


class LapBase(BaseModel):
    pass


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
    id: uuid.UUID
    track_id: uuid.UUID
    car_id: uuid.UUID
    laps: list[Lap]

    class Config:
        orm_mode = True


class TrackBase(BaseModel):
    pass


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
    name: str
    type: str


class CarCreate(CarBase):
    pass


class Car(IdBase, CarBase):
    class Config:
        orm_mode = True
