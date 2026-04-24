import os

from app.core.config import settings

ALLOWED_UPLOAD_FILE_TYPES = {
    "image/png",
    "image/jpg",
    "image/jpeg",
}
ALLOWED_UPLOAD_FILES_TOTAL_SIZE = 5 * 1024 * 1024
FILE_UPLOADS_DIR = os.path.join(settings.STATIC_DIR, "uploads")