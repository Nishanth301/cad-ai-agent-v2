from pathlib import Path
import shutil
import uuid


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def save_upload(upload_file):

    extension = Path(upload_file.filename).suffix

    filename = f"{uuid.uuid4()}{extension}"

    file_path = UPLOAD_DIR / filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return str(file_path)
