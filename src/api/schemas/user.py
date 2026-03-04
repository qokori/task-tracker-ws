from uuid import UUID

from pydantic import BaseModel, EmailStr

from src.api.schemas.base import DateTime


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
