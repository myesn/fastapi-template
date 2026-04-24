from fastapi import APIRouter

from app.api.routers import utils, private, file, user
from app.core.config import settings

api_router = APIRouter()
api_router.include_router(utils.router)
api_router.include_router(file.router)
api_router.include_router(user.router)

if settings.ENVIRONMENT == "local":
    api_router.include_router(private.router)
