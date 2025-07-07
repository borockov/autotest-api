from pydantic import BaseModel, HttpUrl, Field, ConfigDict, EmailStr
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema

class Exercise(BaseModel):
    """
    Описание структуры запроса
    """
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int =Field(alias="minScore")
    order_index: int =Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий по ID курса.
     """
    course_id: str = Field(alias="courseId")

class GetExercisesResponseSchema(BaseModel):
    """
    Ответ от сервера на запрос всех упражнений
    """
    exercises: list[Exercise]

class CreateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создания упражнений в курсе
    """
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class UpdateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнений в курсе
    """
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")