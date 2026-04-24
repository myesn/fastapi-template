import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import SQLModel, Field, Column, TIMESTAMP

from app.utils.datetime_utils import get_datetime_now_with_tz


class UserBase(SQLModel):
    name: str
    extra: dict | None = Field(default=None, sa_type=JSONB, nullable=True)


class User(UserBase, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid7, nullable=False)
    created_at: datetime = Field(
        default_factory=get_datetime_now_with_tz,
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False))
    updated_at: datetime | None = Field(
        default=None,
        sa_column=Column(TIMESTAMP(timezone=True), nullable=True))
