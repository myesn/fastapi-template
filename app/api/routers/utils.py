from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(prefix="/utils", tags=["utils"])


@router.get("/environment")
async def get_environment() -> str:
    return settings.ENVIRONMENT


@router.get("/health-check")
async def health_check() -> bool:
    return True
