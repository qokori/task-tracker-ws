from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.api.schemas.task import (
    TaskCreateSchema,
    TaskFetchListParamsSchema,
    TaskResponseSchema,
    TaskUpdateSchema,
)
from src.models.task import TaskTable
from src.models.user import UserTable


class TaskRepository:
    async def create(
        self,
        session: AsyncSession,
        input_dto: TaskCreateSchema,
    ) -> TaskResponseSchema:
        data = input_dto.model_dump()
        assignee_ids = data.pop("assignees", [])

        task = TaskTable(**data)

        if assignee_ids:
            users_stmt = select(UserTable).where(UserTable.id.in_(assignee_ids))
            users = await session.scalars(users_stmt)
            task.assignees.extend(users.all())

        session.add(task)
        await session.flush()
        await session.refresh(task, attribute_names=["assignees"])
        return TaskResponseSchema.model_validate(task)

    async def fetch_list(
        self,
        session: AsyncSession,
        input_dto: TaskFetchListParamsSchema,
    ) -> list[TaskResponseSchema]:
        stmt = (
            select(TaskTable)
            .options(selectinload(TaskTable.assignees))
            .order_by(TaskTable.id)
        )

        if input_dto.limit:
            stmt = stmt.limit(input_dto.limit)
        if input_dto.offset:
            stmt = stmt.offset(input_dto.offset)

        result = await session.execute(stmt)
        return [TaskResponseSchema.model_validate(t) for t in result.scalars().all()]

    async def fetch_by_id(
        self,
        session: AsyncSession,
        task_id: UUID,
    ) -> TaskResponseSchema | None:
        stmt = (
            select(TaskTable)
            .where(TaskTable.id == task_id)
            .options(selectinload(TaskTable.assignees))
        )
        task = await session.scalar(stmt)

        return TaskResponseSchema.model_validate(task) if task else None

    async def update(
        self,
        session: AsyncSession,
        task_id: UUID,
        input_dto: TaskUpdateSchema,
    ) -> TaskResponseSchema:
        stmt = (
            select(TaskTable)
            .where(TaskTable.id == task_id)
            .options(selectinload(TaskTable.assignees))
        )
        task = await session.scalar(stmt)

        data = input_dto.model_dump(exclude_unset=True)

        if "assignees" in data:
            assignee_ids = data.pop("assignees")
            users_stmt = select(UserTable).where(UserTable.id.in_(assignee_ids))
            users = await session.scalars(users_stmt)
            task.assignees = list(users.all())

        for field, value in data.items():
            setattr(task, field, value)

        await session.flush()
        await session.refresh(task, attribute_names=["assignees"])
        return TaskResponseSchema.model_validate(task)

    async def delete(
        self,
        session: AsyncSession,
        task_id: UUID,
    ) -> None:
        task = await session.get(TaskTable, task_id)
        if task:
            await session.delete(task)
            await session.flush()
