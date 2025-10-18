import uuid

from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError

class UserSchema(BaseModel):
    """
    Модель данных пользователя /api/v1/users
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="LastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Модель запроса на создание пользователя /api/v1/users
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Ответ с данными созданного пользователя, наследуем модель UserSchema
    """
    user: UserSchema