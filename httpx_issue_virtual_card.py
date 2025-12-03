"""Создаёт пользователя, создаёт дебетовый счёт и выпускает виртуальную карту"""

import httpx
import random

user_random = str(random.randint(1, 9999)).zfill(4)
print("Номер случайного пользователя :", user_random)
print("=========================================================================== 00")

# Шаг 1. Создание пользователя
create_user_payload = {
  "email": "httpx_get_"+user_random+"@example.com",
  "lastName": "Тест_"+user_random,
  "firstName": "Проба_"+user_random,
  "middleName": "Учеба_"+user_random,
  "phoneNumber": "+70000000"+user_random
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Статус создания нового пользователя :", create_user_response.status_code)
print("Создан новый пользователь :", create_user_response_data)
print("=========================================================================== 01")

# Шаг 2. Открытие дебетового счёта
open_deposit_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}

open_deposit_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-debit-card-account",
                                        json=open_deposit_account_payload)

open_deposit_account_response_data = open_deposit_account_response.json()
print("Статус создания нового дебетового счёта карты :", open_deposit_account_response.status_code)
print("Создан новый дебетовый счёт карты :", open_deposit_account_response_data)
print("=========================================================================== 02")

# Шаг 3. Выпуск виртуальной карты
issue_virtual_card_payload = {
    "userId": create_user_response_data["user"]["id"],
    "accountId": open_deposit_account_response_data["account"]["id"]
}

issue_virtual_card_response = httpx.post("http://localhost:8003/api/v1/cards/issue-virtual-card",
                                        json=issue_virtual_card_payload)

issue_virtual_card_response_data = issue_virtual_card_response.json()
print(issue_virtual_card_payload)
print("Статус создания виртуальной карты :", issue_virtual_card_response.status_code)
print("Создана новая виртуальная карта :", issue_virtual_card_response_data)
print("=========================================================================== 03")

