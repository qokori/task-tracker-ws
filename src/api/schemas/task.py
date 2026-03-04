from uuid import UUID

from pydantic import BaseModel

from src.api.schemas.base import Pagination, DateTime


class TaskCreate(BaseModel):
    title: str
    description: str
    assignees: list[UUID]
    status: str


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    assignees: list[UUID] | None = None
    status: str | None = None


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str
    assignees: list[UUID]
    status: str
    created_at: DateTime
    updated_at: DateTime


class FetchListParams(Pagination):
    pass
