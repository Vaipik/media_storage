from uuid import UUID

from fastapi import APIRouter

from ..requests.event import EventPost


event_router = APIRouter(
    prefix="/events",
    tags=["Events"],
)


@event_router.get("/")
async def get_events(skip: int = 0, limit: int = 5):
    """Return an array of all events"""
    pass


@event_router.post("/")
async def create_event(event: EventPost):
    """Creating new event"""
    return event


@event_router.get("/{uuid}")
async def get_event(uuid: UUID):
    return uuid
