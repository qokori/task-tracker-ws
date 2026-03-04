from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.task import (
    TaskCreateSchema,
    TaskFetchListParamsSchema,
    TaskResponseSchema,
    TaskUpdateSchema,
)
from src.repositories.task import TaskRepository


class TaskService:
    def __init__(self, session: AsyncSession, repository: TaskRepository) -> None:
        self._repository = repository
        self._session = session

    async def create(self, input_dto: TaskCreateSchema) -> TaskResponseSchema:
        task = await self._repository.create(self._session, input_dto)
        await self._session.commit()
        return task

    async def fetch_list(
        self, params: TaskFetchListParamsSchema
    ) -> list[TaskResponseSchema]:
        return await self._repository.fetch_list(self._session, params)

    async def fetch_by_id(self, task_id: UUID) -> TaskResponseSchema:
        task = await self._repository.fetch_by_id(self._session, task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {task_id} not found",
            )
        return task

    async def update(
        self,
        task_id: UUID,
        input_dto: TaskUpdateSchema,
    ) -> TaskResponseSchema:
        await self.fetch_by_id(task_id)

        task = await self._repository.update(self._session, task_id, input_dto)
        await self._session.commit()
        return task

    async def delete(self, task_id: UUID) -> None:
        await self.fetch_by_id(task_id)
        await self._repository.delete(self._session, task_id)
        await self._session.commit()
