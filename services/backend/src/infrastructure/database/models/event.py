import datetime
import enum
import uuid
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .base import Base


class Event(Base):
    __tablename__ = "events"

    title: Mapped[str]
    description: Mapped[Optional[str]]
    date: Mapped[Optional[datetime.date]]
