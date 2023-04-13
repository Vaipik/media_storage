from typing import Optional

from pydantic import BaseModel


class MediaFile(BaseModel):
    description: Optional[str]
    order: Optional[int]
