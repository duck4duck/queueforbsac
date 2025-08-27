from datetime import datetime
from symtable import Class

from sqlalchemy import DATETIME, DateTime, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(
        primary_key=True, unique=True, nullable=False, autoincrement=True
    )


user_event_table = Table(
    "user_event",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("event_id", ForeignKey("events.id")),
)


class User(Base):
    __tablename__ = "users"
    name: Mapped[str]
    photo_url: Mapped[str]
    events: Mapped[list["Event"]] = relationship(
        "Event", secondary=user_event_table, back_populates="users"
    )


class Subject(Base):
    __tablename__ = "subjects"
    subject_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    events: Mapped[list["Event"]] = relationship("Event", back_populates="subject")


class Event(Base):
    __tablename__ = "events"
    name: Mapped[str]
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    subject: Mapped["Subject"] = relationship("Subject", back_populates="events")
    users: Mapped[list["User"]] = relationship(
        "User", secondary=user_event_table, back_populates="events"
    )
