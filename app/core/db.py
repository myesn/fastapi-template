from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.config import settings

async_engine = create_async_engine(str(settings.SQLALCHEMY_DATABASE_URI))
# https://github.com/fastapi/fastapi/discussions/6458#discussioncomment-9855960
AsyncSessionMaker = async_sessionmaker(async_engine, class_=AsyncSession)
