from typing import Sequence
from uuid import UUID
from src.models.task import TaskStatus
from pydantic import BaseModel

from src.api.schemas.base import Pagination, DateTime


class TaskCreate(BaseModel):
    title: str
    description: str
    assignees: Sequence[UUID]
    status: TaskStatus


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    assignees: Sequence[UUID] | None = None
    status: TaskStatus | None = None


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str
    assignees: Sequence[UUID]
    status: TaskStatus
    created_at: DateTime
    updated_at: DateTime


class FetchListParams(Pagination):
    pass
