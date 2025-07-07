from pydantic import BaseModel, HttpUrl, Field, ConfigDict, EmailStr
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """


    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    previewFile: FileSchema  # Вложенная структура файла
    estimatedTime: str
    createdByUser: UserSchema   # Вложенная структура пользователя

class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    user_id: str = Field(alias="userId")

class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")  # <-- важно
    created_by_user_id: str = Field(alias="createdByUserId")
class UpdateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    last_name:str|None = Field(alias="lastName")
    first_name:str|None = Field(alias="firstName")
    middle_name: str|None = Field(alias="middleName")

class CreateCourseResponseSchema(BaseModel):
    course: CourseSchema