import httpx

login_payload = {
  "email": "testuser@mail.ru",
  "password": "159951"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Код ответа:", login_response.status_code)
print("Ответ с JSON токенами:", login_response_data)

usr_headers = {
    "Authorization": f'Bearer {login_response_data['token']['accessToken']}'
}

user_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=usr_headers)

print("Код ответа:", user_me.status_code)
print("Ответ содержит JSON с данными пользователя:",user_me.json())