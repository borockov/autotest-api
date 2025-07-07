from pydantic import BaseModel, HttpUrl

class FileSchema(BaseModel):
    id:str
    url: HttpUrl
    filename: str
    directory:str

class CreateFileRequestSchema(BaseModel):
    filename:str
    directory:str
    upload_file:str

class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema