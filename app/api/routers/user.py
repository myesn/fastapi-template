import uuid

from fastapi import APIRouter, status

from app import crud
from app.api.deps import AsyncSessionDep
from app.dtos import UserOut, UserCreate, UserUpdate
from app.models import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
async def get_users(
        session: AsyncSessionDep, ) -> list[UserOut]:
    return _users_to_dtos(await crud.get_users(session=session))


@router.get("/{user_id}")
async def get_user_by_id(session: AsyncSessionDep, user_id: uuid.UUID) -> UserOut:
    return _user_to_dto(await crud.get_user_by_id(session=session, id=user_id))


@router.post("", status_code=status.HTTP_204_NO_CONTENT)
async def create_user(session: AsyncSessionDep, dto: UserCreate) -> None:
    await crud.create_user(session=session, dto=dto)


@router.patch("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(session: AsyncSessionDep, user_id: uuid.UUID, dto: UserUpdate) -> None:
    await crud.update_user(session=session, id=user_id, dto=dto)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(session: AsyncSessionDep, user_id: uuid.UUID) -> None:
    await crud.delete_user(session=session, id=user_id)


def _users_to_dtos(users: list[User]) -> list[UserOut]:
    return [UserOut(**user.model_dump()) for user in users if user]


def _user_to_dto(user: User | None) -> UserOut | None:
    return UserOut(**user.model_dump()) if user else None
