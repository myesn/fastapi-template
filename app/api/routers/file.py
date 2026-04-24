import os.path
import uuid
from datetime import date
from pathlib import Path
from typing import Annotated
from urllib.parse import urljoin, urlencode

from fastapi import APIRouter, UploadFile, File, HTTPException, Query, status
from fastapi.responses import FileResponse

from app.const import ALLOWED_UPLOAD_FILE_TYPES, ALLOWED_UPLOAD_FILES_TOTAL_SIZE, FILE_UPLOADS_DIR
from app.core.config import settings
from app.utils.file_utils import save_to_disk

router = APIRouter(prefix="/files", tags=["file"])


@router.get("")
async def get_file(path: Annotated[str, Query(min_length=1)]) -> FileResponse:
    return FileResponse(os.path.join(FILE_UPLOADS_DIR, path))


@router.post("")
async def uploads(
        files: Annotated[list[UploadFile], File()]
) -> list[str]:
    _check_upload_files(files)
    file_paths = _save_files(files)
    file_links = [file_path_to_link(file_path) for file_path in file_paths]
    return file_links


def file_path_to_link(file_path) -> str:
    path = "/".join((settings.API_STR, router.prefix[1:]))
    query = urlencode({"path": file_path})
    return urljoin(settings.APP_URL, f"{path}?{query}")


def _save_files(upload_files: list[UploadFile]) -> list[str]:
    today_dir = str(date.today())
    save_dir = os.path.join(FILE_UPLOADS_DIR, today_dir)
    os.makedirs(save_dir, exist_ok=True)

    file_paths = []
    for upload_file in upload_files:
        old_file_suffix = Path(upload_file.filename).suffix
        new_file_name = f"{uuid.uuid7()}{old_file_suffix}"
        new_file_path = os.path.join(save_dir, new_file_name)

        save_to_disk(new_file_path, upload_file)
        file_paths.append(os.path.join(today_dir, new_file_name))
    return file_paths


def _check_upload_files(upload_files: list[UploadFile]) -> None:
    _check_upload_files_empty(upload_files)
    _check_upload_files_type(upload_files)
    check_upload_files_total_size(upload_files)


def _check_upload_files_empty(upload_files: list[UploadFile]) -> None:
    if upload_files[0].size == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="未上传任何文件")


def _check_upload_files_type(upload_files: list[UploadFile]) -> None:
    for upload_file in upload_files:
        _check_upload_file_type(upload_file)


def _check_upload_file_type(upload_file: UploadFile) -> None:
    if upload_file.content_type not in ALLOWED_UPLOAD_FILE_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"不允许的文件类型: {upload_file.filename}")


def check_upload_files_total_size(upload_files: list[UploadFile]) -> None:
    total_size = sum([upload_file.size for upload_file in upload_files
                      if upload_file.size is not None])
    if total_size > ALLOWED_UPLOAD_FILES_TOTAL_SIZE:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"总文件大小超过限制")
