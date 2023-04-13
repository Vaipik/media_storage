from fastapi import FastAPI

from src.presentation.controllers.event import event_router
from src.presentation.controllers.media import file_router

app = FastAPI()

app.include_router(event_router)
app.include_router(file_router)
