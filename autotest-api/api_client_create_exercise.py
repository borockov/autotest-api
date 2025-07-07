from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.files.files_client import get_files_client, CreateFileRequestSchema
from clients.courses.courses_client import get_courses_client, CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client, CreateExercisesRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    first_name="string",
    last_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)

auth_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(auth_user)
courses_client = get_courses_client(auth_user)
exercises_client = get_exercises_client(auth_user)

file_request = CreateFileRequestSchema(
    filename="images.png",
    directory="courses",
    upload_file="./testdata/files/images.png"
)
file_response = files_client.create_file(file_request)
print("Create file data:", file_response)

course_request = CreateCourseRequestSchema(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    preview_file_id=file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
course_response = courses_client.create_course(course_request)
print("Create course data:", course_response)

exercise_request = CreateExercisesRequestSchema(
    title="Exercise 1",
    courseId=course_response.course.id,
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="5 minutes"
)
exercise_response = exercises_client.create_exercises_api(exercise_request)
print("Create exercise data:", exercise_response.json())