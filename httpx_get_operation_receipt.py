"""Создаёт пользователя, создаёт кредитную карту, совершает покупку и получает чек по операции"""

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

# Шаг 2. Открытие кредитового счёта
open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}

open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",
                                        json=open_credit_card_account_payload)

open_credit_card_account_response_data = open_credit_card_account_response.json()
print("Статус создания нового кредитового счёта карты :", open_credit_card_account_response.status_code)
print("Создан новый кретовый счёт карты :", open_credit_card_account_response_data)
print("=========================================================================== 02")

# Шаг 3. Совершает покупку
make_purchase_operation_payload = {
  "status": "COMPLETED",
  "amount": int(user_random),
  "cardId": open_credit_card_account_response_data['account']['cards'][0]['id'],
  "accountId": open_credit_card_account_response_data['account']['id'],
  "category": "Покупка на сумму "+ user_random
}
make_purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=make_purchase_operation_payload)

make_purchase_operation_response_data = make_purchase_operation_response.json()
print("Статус совершения покупки :", make_purchase_operation_response.status_code)
print("Совершает покупку :", make_purchase_operation_response_data)
print("=========================================================================== 03")

# Шаг 4. Получает чек по операции
get_operation_receipt_response = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{make_purchase_operation_response_data['operation']['id']}")
get_operation_receipt_response_data = get_operation_receipt_response.json()
print("Статус получения чека по операции :", get_operation_receipt_response.status_code)
print("Получает чек по операции :", get_operation_receipt_response_data)
print("=========================================================================== 04")
