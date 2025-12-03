import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)     # 200
print(response.json())          # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
print(response.text)
print("=========================================================================== 01")

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
print(response.json())
print("=========================================================================== 02")

data = {"username": "test_user", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
print(response.json())
print(response.request.headers)
print("=========================================================================== 03")

response = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1")
print(response.status_code)
print(response.json())
print("=========================================================================== 04")

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.request.url)
print(response.request.url.query)
print(response.status_code)
print(response.json())
print("=========================================================================== 05")

files = {"file": ("http_example.txt", open("httpx_example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.status_code)
print(response.json())
print(response.request.headers)
print("=========================================================================== 06")

with httpx.Client() as client:
    response1 = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = httpx.get("https://jsonplaceholder.typicode.com/todos/2")
print(response1.status_code)
print(response2.status_code)
print(response1.json())
print(response2.json())
print("=========================================================================== 07")

client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
print(response1.status_code)
print(response2.status_code)
print(response1.json())
print(response2.json())
print(response1.headers)
print(response2.headers)
print("=========================================================================== 08")

client = httpx.Client(base_url="https://jsonplaceholder.typicode.com", headers={"Authorization": "Bearer my_secret_token"})
response1 = client.get("/todos/1")
response2 = client.get("/todos/2")
print(response1.status_code)
print(response2.status_code)
print(response1.json())
print(response2.json())
print(response1.headers)
print(response2.headers)
print("=========================================================================== 09")

response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
print(response.request.url)
print(response.status_code)
print(response.json())
print("=========================================================================== 10")

try:
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")
print("=========================================================================== 11")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout as e:
    print(f"Запрос превысил лимит времени: {e}")
print("=========================================================================== 12")
