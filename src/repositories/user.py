from src.api.schemas.user import (
    UserLoginSchema,
    UserRegisterSchema,
    UserResponseAccessTokenSchema,
    UserResponseSchema,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.user import UserTable
from src.db.core.exceptions.exceptions import UniqueConstraint, DoesNotExists
from src.db.core.security.auth import (
    hash_password,
    verify_password,
    create_access_token,
)


class UserRepository:
    async def register(
        self, input_dto: UserRegisterSchema, session: AsyncSession
    ) -> UserResponseSchema:
        res = await session.execute(
            select(UserTable).where(UserTable.username == input_dto.username)
        )
        if res.scalar_one_or_none():
            raise UniqueConstraint("Пользователь с таким username уже существует")
        user = UserTable(
            username=input_dto.username,
            hashed_password=hash_password(input_dto.password),
            email=input_dto.email,
            display_name=input_dto.display_name,
        )
        session.add(user)
        await session.flush()
        await session.refresh(user)
        return UserResponseSchema(
            id=user.id,
            username=user.username,
            display_name=user.display_name,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    async def login(
        self, input_dto: UserLoginSchema, session: AsyncSession
    ) -> UserResponseAccessTokenSchema:
        baby = (
            UserTable.email == input_dto.email
            if input_dto.email
            else UserTable.username == input_dto.username
        )
        res = await session.execute(select(UserTable).where(baby))
        user = res.scalar_one_or_none()
        if not user or not verify_password(input_dto.password, user.hashed_password):
            raise DoesNotExists("Пользователя с такими данными не найден")
        token = create_access_token(subject=user.id, extra=dict(username=str(user.username)))
        return UserResponseAccessTokenSchema(access_token=token, user_id=user.id)
