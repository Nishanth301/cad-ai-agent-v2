from fastapi import APIRouter, UploadFile, File

from app.utils.file_utils import save_upload

router = APIRouter()


@router.post("/upload")
async def upload_image(
    file: UploadFile = File(...)
):

    file_path = save_upload(file)

    return {
        "filename": file.filename,
        "saved_as": file_path
    }
