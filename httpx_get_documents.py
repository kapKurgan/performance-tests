"""Создаёт пользователя, создаёт кредитовый счёт и получает документы"""

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
print("Создан новый кредитовый счёт карты :", open_credit_card_account_response_data)
print("=========================================================================== 02")

# Шаг 3. Получение документов тариф
get_tariff_document_response = httpx.get(f"http://localhost:8003/api/v1/documents/tariff-document/"
                                         f"{open_credit_card_account_response_data['account']['id']}")

get_tariff_document_response_data = get_tariff_document_response.json()
print("Статус GET на тариф документа :", get_tariff_document_response.status_code)
print("Создана новый тариф документа :", get_tariff_document_response_data)
print("=========================================================================== 03")

# Шаг 4. Получение документов контракт
get_contract_document_response = httpx.get(f"http://localhost:8003/api/v1/documents/contract-document/"
                                         f"{open_credit_card_account_response_data['account']['id']}")

get_contract_document_response_data = get_contract_document_response.json()
print("Статус GET на контракт документа :", get_contract_document_response.status_code)
print("Создана новый контракт документа :", get_contract_document_response_data)
print("=========================================================================== 04")

