import uuid

from pydantic import BaseModel


class SessionBase(BaseModel):
    laps: int


class SessionCreate(SessionBase):
    pass


class Session(SessionBase):
    id: uuid.UUID

    class Config:
        orm_mode = True
