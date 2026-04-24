import uuid

from fastapi import status, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.dtos import UserCreate, UserUpdate
from app.models import User
from app.utils.datetime_utils import get_datetime_now_with_tz


async def get_users(
        *,
        session: AsyncSession) -> list[User]:
    statement = select(User).order_by(User.created_at)
    users: list[User] = (await session.exec(statement)).all()
    return users


async def get_user_by_id(
        *,
        session: AsyncSession,
        id: uuid.UUID,
        check: bool = True) -> User | None:
    entity = await session.get(User, id)
    _check(check, entity, f"找不到用户，users.id={id}")
    return entity


async def get_user_by_name(
        *,
        session: AsyncSession,
        name: str,
        check: bool = True) -> User | None:
    statement = select(User).where(User.name == name)
    entity: User = (await session.exec(statement)).first()
    _check(check, entity, f"找不到用户，users.name={name}")
    return entity


async def create_user(
        *,
        session: AsyncSession,
        dto: UserCreate) -> User:
    entity = User.model_validate(dto)
    name_exists = await get_user_by_name(session=session, name=dto.name, check=False)
    if name_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"用户名称 {dto.name} 已存在")
    session.add(entity)
    await session.commit()
    await session.refresh(entity)
    return entity


async def update_user(
        *,
        session: AsyncSession,
        id: uuid.UUID,
        dto: UserUpdate) -> User:
    entity = await get_user_by_id(session=session, id=id)
    name_exists = await get_user_by_name(session=session, name=dto.name, check=False)
    if name_exists and name_exists.id != entity.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"用户名称 {dto.name} 已存在")
    user_data = dto.model_dump(exclude_unset=True)
    entity.sqlmodel_update(user_data, update={"updated_at": get_datetime_now_with_tz()})
    await session.commit()
    await session.refresh(entity)
    return entity


async def delete_user(
        *,
        session: AsyncSession,
        id: uuid.UUID) -> None:
    entity = await get_user_by_id(session=session, id=id, check=False)
    if not entity:
        return
    await session.delete(entity)
    await session.commit()


def _check[TEntity](
        check: bool,
        entity: TEntity,
        error_message: str | None) -> None:
    if check and not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_message)
