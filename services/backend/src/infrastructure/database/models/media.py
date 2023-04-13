import enum
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .base import Base


class MediaType(str, enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"


class MediaFile(Base):
    __tablename__ = "media_files"

    description: Mapped[Optional[str]]
    type: Mapped[MediaType]
