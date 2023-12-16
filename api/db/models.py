import uuid

from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import Base


class Id:
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)


class Session(Id, Base):
    __tablename__ = "sessions"

    track_id = Column(UUID(as_uuid=True), ForeignKey("tracks.id"))
    car_id = Column(UUID(as_uuid=True), ForeignKey("cars.id"))

    track = relationship("Track", back_populates="sessions")
    car = relationship("Car", back_populates="sessions")
    laps = relationship("Lap", back_populates="session")


class Lap(Id, Base):
    __tablename__ = "laps"

    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.id"))
    time = Column(Float)

    session = relationship("Session", back_populates="laps")


class Game(Id, Base):
    __tablename__ = "games"

    name = Column(String, unique=True, index=True, nullable=False)

    tracks = relationship("Track", back_populates="game")
    cars = relationship("Car", back_populates="game")


class Track(Id, Base):
    __tablename__ = "tracks"

    name = Column(String, unique=True, index=True, nullable=False)
    country = Column(String)

    game_id = Column(UUID(as_uuid=True), ForeignKey("games.id"))

    game = relationship("Game", back_populates="tracks")
    sessions = relationship("Session", back_populates="track")


class Car(Id, Base):
    __tablename__ = "cars"

    make = Column(String)
    model = Column(String)
    car_class = Column(String)

    game_id = Column(UUID(as_uuid=True), ForeignKey("games.id"))

    game = relationship("Game", back_populates="cars")
    sessions = relationship("Session", back_populates="car")
