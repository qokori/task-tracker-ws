from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseTable(DeclarativeBase):
    pass


class UUIDMixin:
    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        nullable=False,
        sort_order=-1,
    )


class TimeStampMixin:
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        sort_order=100,
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),
        sort_order=101,
    )
