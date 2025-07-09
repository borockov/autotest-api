import httpx
from tools.fakers import fake
payload = {
    "email":fake.email(),
    "password":"1234",
    "lastName":"Бороков",
    "firstName":"Тимур",
    "middleName":"Хамидбиевич"
}
response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=payload)
print(response.status_code)
print(response.json())