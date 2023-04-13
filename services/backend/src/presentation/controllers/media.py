import shutil
from pathlib import Path

from fastapi import APIRouter, UploadFile

from src.presentation.responses.media import FileResponse


file_router = APIRouter(
    prefix="/files",
    tags=["Event files"]
)


@file_router.get(
    "/",
    response_model=list[FileResponse]
)
async def get_uploaded_files(skil: int = 0, limit: int = 5):
    """Return"""
    pass


@file_router.get(
    "/{uuid}/",
    response_model=FileResponse
)
async def get_uploaded_file():
    pass


@file_router.post(
    "/uploadfiles/",
    # response_model=list[FileResponse]
)
async def upload_file(file: UploadFile):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"msg": file.filename}
