from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, PlainSerializer

DateTime = Annotated[
    datetime,
    PlainSerializer(
        lambda value: value.strftime("%Y-%m-%d %H:%M:%S"),
        return_type=str,
    ),
]


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class Pagination(BaseSchema):
    offset: int | None = None
    limit: int | None = None
