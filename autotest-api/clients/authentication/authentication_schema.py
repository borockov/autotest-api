from pydantic import BaseModel, Field, EmailStr

class TokenSchema(BaseModel):
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str = EmailStr
    password: str

class LoginResponseSchema(BaseModel):
    """
    Модель токена
    """
    token: TokenSchema

class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token:str = Field(alias="refreshToken")