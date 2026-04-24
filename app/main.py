from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.api.main import api_router
from app.core.config import settings

app = FastAPI(
    title=f'{settings.PROJECT_NAME} - {settings.ENVIRONMENT}',
    openapi_url=f'{settings.API_STR}/openapi.json',
)

origins = (
    "http://localhost:3000",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=("*",),
    allow_headers=("*",),
)

app.include_router(api_router, prefix=settings.API_STR)


@app.get("/", include_in_schema=False)
async def index():
    if settings.ENVIRONMENT == "local":
        return RedirectResponse(app.docs_url or app.redoc_url or "")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
