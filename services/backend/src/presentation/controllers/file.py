from fastapi import APIRouter, UploadFile


file_router = APIRouter(
    prefix="/files",
    tags=["Event files"]
)


@file_router.post("/")
async def upload_file(file: UploadFile):
    with open("destination.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.file}
