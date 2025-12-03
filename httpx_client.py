"""7.3.1 Знакомство с HTTP API клиентами"""

import httpx
import random

user_random = str(random.randint(1, 9999)).zfill(4)
print("Номер случайного пользователя :", user_random)
print("=========================================================================== 00")

client = httpx.Client(base_url="http://localhost:8003")
payload = {
  "email": "httpx_get_"+user_random+"@example.com",
  "lastName": "Тест_"+user_random,
  "firstName": "Проба_"+user_random,
  "middleName": "Учеба_"+user_random,
  "phoneNumber": "+70000000"+user_random
}
create_user_response = client.post("/api/v1/users", json=payload, timeout=10, headers={"Autorization": "Bearer ..."})
print("Статус создания нового пользователя :", create_user_response.status_code)
print("Создан новый пользователь :", create_user_response.text)
print("Заголовок запроса :", create_user_response.request.headers)
print("=========================================================================== 01")
