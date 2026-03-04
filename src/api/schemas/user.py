from uuid import UUID

from pydantic import EmailStr

from src.api.schemas.base import BaseSchema, DateTime


class UserRegisterSchema(BaseSchema):
    username: str
    email: EmailStr
    password: str
    display_name: str | None = None


class UserLoginSchema(BaseSchema):
    username: str
    password: str


class UserResponseAccessTokenSchema(UserRegisterSchema):
    access_token: str
    user_id: UUID


class UserUpdateSchema(BaseSchema):
    username: str | None = None
    password: str | None = None
    display_name: str | None = None
    email: EmailStr | None = None


class UserResponseSchema(BaseSchema):
    id: UUID
    username: str
    display_name: str | None = None
    email: EmailStr
    created_at: DateTime
    updated_at: DateTime
