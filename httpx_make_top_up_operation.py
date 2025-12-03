"""Создаёт пользователя, создаёт дебетовую карту и пополняет счет"""

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
open_debit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}

open_debit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-debit-card-account",
                                        json=open_debit_card_account_payload)

open_debit_card_account_response_data = open_debit_card_account_response.json()
print("Статус создания нового дебетового счёта карты :", open_debit_card_account_response.status_code)
print("Создан новый дебетовый счёт карты :", open_debit_card_account_response_data)
print("=========================================================================== 02")

# Шаг 3. Пополнение счета
make_top_up_operation_payload = {
  "status": "COMPLETED",
  "amount": int(user_random),
  "cardId": open_debit_card_account_response_data['account']['cards'][0]['id'],
  "accountId": open_debit_card_account_response_data['account']['id']
}
make_top_up_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-top-up-operation", json=make_top_up_operation_payload)

make_top_up_operation_response_data = make_top_up_operation_response.json()
print("Статус пополнения счета карты :", make_top_up_operation_response.status_code)
print("Счет карты пополнен :", make_top_up_operation_response_data)
print("=========================================================================== 03")

