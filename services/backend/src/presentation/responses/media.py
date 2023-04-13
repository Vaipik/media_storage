import enum
from typing import Optional
import uuid

from pydantic import BaseModel


class MediaType(str, enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"


class FileResponse(BaseModel):
    id: uuid.UUID
    description: Optional[str]
    url: str
    type: MediaType

    class Config:
        orm_mode = True
