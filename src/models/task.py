from enum import StrEnum

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseTable, TimeStampMixin, UUIDMixin

from .user import user_task_association


class TaskStatus(StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class TaskTable(BaseTable, UUIDMixin, TimeStampMixin):
    __tablename__ = "tasks"

    title: Mapped[str] = mapped_column(String(255), index=True)
    description: Mapped[str | None] = mapped_column(Text)
    status: Mapped[TaskStatus] = mapped_column(default=TaskStatus.PENDING)

    assignees: Mapped[list["UserTable"]] = relationship(
        secondary=user_task_association,
        back_populates="tasks",
    )
