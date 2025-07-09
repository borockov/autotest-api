import httpx
from tools.fakers import fake
#Создаем пользователя
create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users",json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user successful:',create_user_response.status_code)
print(create_user_response_data['user']['email'])

#Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login",
                            json=login_payload)
login_response_data = login_response.json()
print("Autentification successful:",login_response.status_code)

#Выполняем частичное обновление данные у созданного ранее пользователя
patch_payload = {
    "email": fake.email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

patch_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

patch_response = httpx.patch(
    f"http://127.0.0.1:8000/api/v1/users/{create_user_response_data['user']['id']}",
    json=patch_payload,
    headers=patch_headers
)
patch_response_data = patch_response.json()
print("update user successful:", patch_response.status_code)
print('user email update:',patch_response_data['user']['email'])