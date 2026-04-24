import uuid
from datetime import datetime
from typing import TypeVar

from app.models import UserBase

# 弃用，接口需要响应数据时，直接返回数据即可，如无数据则不返回
# # 异常时直接抛出 fastapi.HTTPException，没有异常时返回此类型
# class APIResponse[TData](BaseModel):
#     # success: bool
#     data: TData | None = None
#     # error_message: str | None = None

T = TypeVar("T")


class UserOut(UserBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
