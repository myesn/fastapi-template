import shutil

from fastapi import UploadFile


def save_to_disk(new_file_path: str, upload_file: UploadFile) -> None:
    try:
        with open(new_file_path, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()
