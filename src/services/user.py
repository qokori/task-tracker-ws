from sqlalchemy.ext.asyncio import AsyncSession
from src.api.schemas.user import (
    UserLoginSchema,
    UserRegisterSchema,
    UserResponseAccessToken,
    UserResponseSchema,
)
from src.repositories.user import UserRepository


class UserService:
    def __init__(self, session: AsyncSession, repository: UserRepository) -> None:
        self._repository = repository
        self._session = session

    async def register(self, input_dto: UserRegisterSchema) -> UserResponseSchema:
        user = await self._repository.register(
            session=self._session, input_dto=input_dto
        )
        await self._session.commit()
        return user

    async def login(self, input_dto: UserLoginSchema) -> UserResponseAccessToken:
        user = await self._repository.login(session=self._session, input_dto=input_dto)
        await self._session.commit()
        return user
