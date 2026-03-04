from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, PlainSerializer

from src.api.schemas.base import Pagination

DateTime = Annotated[
    datetime,
    PlainSerializer(
        lambda value: value.strftime("%Y-%m-%d %H:%M:%S"), return_type=str
    )
]


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
