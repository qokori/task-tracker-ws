from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, PlainSerializer, EmailStr

DateTime = Annotated[
    datetime,
    PlainSerializer(
        lambda value: value.strftime("%Y-%m-%d %H:%M:%S")
    )
]


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponseAccessToken(UserRegister):
    access_token: str
    user_id: UUID


class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    display_name: str | None = None
    email: EmailStr | None = None


class UserResponse(BaseModel):
    id: UUID
    username: str
    display_name: str | None = None
    email: str
    created_at: DateTime
    updated_at: DateTime
