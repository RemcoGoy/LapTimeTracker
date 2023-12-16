import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class IdBase:
    id: uuid.UUID


class LapBase(BaseModel):
    time: float


class LapCreate(LapBase):
    pass


class LapUpdate(LapBase):
    pass


class Lap(IdBase, LapBase):
    class ConfigDict:
        from_attributes = True


class SessionBase(BaseModel):
    start_time: datetime


class SessionCreate(SessionBase):
    pass


class SessionUpdate(SessionBase):
    pass


class Session(IdBase, SessionBase):
    track_id: uuid.UUID
    car_id: uuid.UUID
    laps: list[Lap]

    class ConfigDict:
        from_attributes = True


class TrackBase(BaseModel):
    name: str
    country: str


class TrackCreate(TrackBase):
    pass


class TrackUpdate(TrackBase):
    name: Optional[str] = None
    country: Optional[str] = None


class Track(IdBase, TrackBase):
    game_id: uuid.UUID

    class ConfigDict:
        from_attributes = True


class GameBase(BaseModel):
    name: str


class GameCreate(GameBase):
    pass


class GameUpdate(GameBase):
    pass


class Game(IdBase, GameBase):
    tracks: list[Track]

    class ConfigDict:
        from_attributes = True


class CarBase(BaseModel):
    make: str
    model: str
    car_class: str


class CarCreate(CarBase):
    pass


class CarUpdate(CarBase):
    make: Optional[str] = None
    model: Optional[str] = None
    car_class: Optional[str] = None


class Car(IdBase, CarBase):
    class ConfigDict:
        from_attributes = True
