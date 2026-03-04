from collections.abc import Sequence
from uuid import UUID

from src.api.schemas.base import BaseSchema, DateTime, Pagination
from src.api.schemas.user import UserResponseSchema
from src.models.task import TaskStatus


class TaskCreateSchema(BaseSchema):
    title: str
    description: str
    assignees: Sequence[UUID] = []
    status: TaskStatus


class TaskUpdateSchema(BaseSchema):
    title: str | None = None
    description: str | None = None
    assignees: Sequence[UUID] | None = None
    status: TaskStatus = TaskStatus.PENDING


class TaskResponseSchema(BaseSchema):
    id: UUID
    title: str
    description: str
    assignees: Sequence[UserResponseSchema]
    status: TaskStatus
    created_at: DateTime
    updated_at: DateTime


class TaskFetchListParamsSchema(Pagination):
    pass
