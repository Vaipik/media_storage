import shutil
from pathlib import Path

from fastapi import APIRouter, UploadFile, Depends

from src.application.google_drive.service import GoogleDrive, BASE_DIR
from src.presentation.responses.media import FileResponse

cloud_storage = GoogleDrive()

file_router = APIRouter(
    prefix="/files",
    tags=["Event files"]
)


@file_router.get(
    "/",
    # response_model=list[FileResponse]
)
async def get_uploaded_files(skil: int = 0, limit: int = 5):
    """Return"""
    cloud_storage.get_files()


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
    uploaded_file = Path(BASE_DIR) / file.filename
    with open(uploaded_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    a = cloud_storage.upload_file(uploaded_file)

    return {"msg": file.filename,
            "a": a
            }
