from uuid import UUID

from pydantic import BaseModel, EmailStr

from src.api.schemas.base import DateTime


class UserRegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    display_name: str | None = None


class UserLoginSchema(BaseModel):
    username: str
    password: str


class UserResponseAccessToken(UserRegisterSchema):
    access_token: str
    user_id: UUID


class UserUpdateSchema(BaseModel):
    username: str | None = None
    password: str | None = None
    display_name: str | None = None
    email: EmailStr | None = None


class UserResponseSchema(BaseModel):
    id: UUID
    username: str
    display_name: str | None = None
    email: str
    created_at: DateTime
    updated_at: DateTime
