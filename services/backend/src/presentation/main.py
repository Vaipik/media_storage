from functools import lru_cache
from typing import Annotated

from fastapi import FastAPI, Depends

from src.config import load_config
from src.presentation.controllers.event import event_router
from src.presentation.controllers.media import file_router

load_config()

app = FastAPI()

app.include_router(event_router)
app.include_router(file_router)

