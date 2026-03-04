from pydantic import BaseModel


class Pagination(BaseModel):
    offset: int | None = None
    limit: int | None = None
