from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.authentication.authentication_client import get_authentication_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import GetUserResponseSchema
from tools.fakers import get_random_email
from tools.assertions.schema import validate_json_schema
from clients.private_http_builder import AuthenticationUserSchema

# 1. Создаём клиента
public_users_client = get_public_users_client()

# 2. Формируем и отправляем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

create_user_response = public_users_client.create_user_api(create_user_request)
parsed_response = CreateUserResponseSchema.model_validate_json(create_user_response.text)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
# 3. Валидируем ответ на создание пользователя
validate_json_schema(instance=parsed_response.model_dump(by_alias=True), schema=create_user_response_schema)

# 4. Извлекаем user_id и email для логина

email = create_user_request.email
password = create_user_request.password

# 5. Авторизуемся, получаем токен
auth_client = get_authentication_client()
login_request = LoginRequestSchema(email=email, password=password)
login_response = auth_client.login(login_request)

# 6. Собираем user-объект для авторизованного клиента
auth_user = AuthenticationUserSchema(
    access_token=login_response.token.access_token,
    refresh_token=login_response.token.refresh_token,
    email=email,
    password=password
)

# 7. Получаем private client
private_users_client = get_private_users_client(auth_user)

# 8. Достаём пользователя по ID
get_user_response = private_users_client.get_user(parsed_response.user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# 9. Валидируем ответ
validate_json_schema(instance=get_user_response.model_dump(by_alias=True), schema=get_user_response_schema)

# 10. Успешно
print("Валидация прошла успешно!")
