from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, PlainSerializer

DateTime = Annotated[
    datetime,
    PlainSerializer(
        lambda value: value.strftime("%Y-%m-%d %H:%M:%S"),
        return_type=str,
    ),
]


class Pagination(BaseModel):
    offset: int | None = None
    limit: int | None = None
