import pytest
from pydantic import BaseModel
from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema

from fixtures.users import UserFixture
from fixtures.files import FileFixture


class CourseFixture:
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)


def function_courses(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture) -> CourseFixture:
    request = CreateCourseRequestSchema(
        previewFileId=function_file.response.file.id,
        createdByUserId=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)
