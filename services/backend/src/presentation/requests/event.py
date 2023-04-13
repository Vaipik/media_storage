from typing import Optional

from pydantic import BaseModel, Field, validator

from src.application.common.constants import event as constants


class EventPost(BaseModel):
    title: str = Field(
        alias="eventTitle"
    )
    description: Optional[str] = Field(
        alias="eventDescription"
    )

    @validator("title")
    def title_length(cls, v):
        title_len = len(v)
        if title_len > constants.EVENT_TITLE_MAX_LENGTH:
            raise ValueError(f"title must be shorter than {constants.EVENT_TITLE_MAX_LENGTH}")

        if title_len < constants.EVENT_TITLE_MIN_LENGTH:
            raise ValueError(f"title must be longer than {constants.EVENT_TITLE_MIN_LENGTH}")

        return v

    @validator("description")
    def description_length(cls, v):
        description_len = len(v)
        if description_len > constants.EVENT_DESCRIPTION_MAX_LENGTH:
            raise ValueError(f"description must be shorter than {constants.EVENT_DESCRIPTION_MAX_LENGTH}")

        return v
