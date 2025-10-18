import httpx

data = {
    "title":"Мой тест",
    "body": "Салам алейкум",
    "userId":99
}

response = httpx.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.status_code)
print(response.json())