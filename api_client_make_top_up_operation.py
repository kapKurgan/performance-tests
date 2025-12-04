from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client

users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
operations_gateway_client = build_operations_gateway_http_client()

# Создаем пользователя
create_user_response = users_gateway_client.create_user()
print('Создаем пользователя:', create_user_response)
print("=========================================================================== 01")

# Ответ на открытие счета дебетовой карты
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(user_id=create_user_response['user']['id'])
print('Ответ на открытие счета дебетовой карты:', open_debit_card_account_response)
print("=========================================================================== 02")

# Ответ на операцию пополнение счета
make_top_up_operation_response = operations_gateway_client.make_top_up_operation(
    card_id=open_debit_card_account_response['account']['cards'][0]['id'],
    account_id=open_debit_card_account_response['account']['id'])
print('Ответ на операцию пополнение счета :', make_top_up_operation_response)
print("=========================================================================== 03")
