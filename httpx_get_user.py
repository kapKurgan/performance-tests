import httpx
import random

user_random = str(random.randint(1, 9999)).zfill(4)
print("Номер случайного пользователя :", user_random)
create_user_payload = {
  "email": "httpx_get_"+user_random+"@example.com",
  "lastName": "Тест_"+user_random,
  "firstName": "Проба_"+user_random,
  "middleName": "Учеба_"+user_random,
  "phoneNumber": "+70000000"+user_random
}

creat_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
creat_user_response_data = creat_user_response.json()
print("Статус создания нового пользователя :", creat_user_response.status_code)
print("Создан новый пользователь :", creat_user_response_data)
print("=========================================================================== 01")

get_user_response = httpx.get(f"http://localhost:8003/api/v1/users/{creat_user_response_data['user']['id']}")
get_user_response_data = get_user_response.json()
print("Статус по GET запросу пользователя :", get_user_response.status_code)
print("Пользователь по GET запросу :", get_user_response_data)
print("=========================================================================== 02")
