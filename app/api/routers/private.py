from fastapi import APIRouter

from app.core.config import settings, Settings

router = APIRouter(prefix="/private", tags=["private"])


@router.get("/settings")
async def get_settings() -> Settings:
    return settings
