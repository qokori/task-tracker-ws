from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseTable, TimeStampMixin, UUIDMixin

user_task_association = Table(
    "user_task_association",
    BaseTable.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("task_id", ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True),
)


class UserTable(BaseTable, UUIDMixin, TimeStampMixin):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    display_name: Mapped[str | None] = mapped_column(String(255), nullable=True)

    tasks: Mapped[list["TaskTable"]] = relationship(
        secondary=user_task_association,
        back_populates="assignees",
    )
