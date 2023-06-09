import enum
import uuid
from typing import Annotated

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

uuid_pk = Annotated[uuid.UUID, mapped_column(primary_key=True, insert_default=uuid.uuid4)]


class MediaType(str, enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"


class BaseModel(DeclarativeBase):
    pass


class Base(BaseModel):
    """
    An abstract base model that makes id field as UUID field as primary key field in models
    """
    __abstract__ = True

    id: Mapped[uuid_pk]
