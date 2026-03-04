from collections.abc import Sequence
from uuid import UUID

from pydantic import BaseModel

from src.api.schemas.base import DateTime, Pagination
from src.models.task import TaskStatus


class TaskCreateSchema(BaseModel):
    title: str
    description: str
    assignees: Sequence[UUID]
    status: TaskStatus


class TaskUpdateSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    assignees: Sequence[UUID] | None = None
    status: TaskStatus | None = None


class TaskResponseSchema(BaseModel):
    id: UUID
    title: str
    description: str
    assignees: Sequence[UUID]
    status: TaskStatus
    created_at: DateTime
    updated_at: DateTime


class TaskFetchListParamsSchema(Pagination):
    pass
