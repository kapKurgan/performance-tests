from clients.http.gateway.users.client import build_users_gateway_http_client

users_gateway_client = build_users_gateway_http_client()

# Отправляем POST запрос на создание пользователя
create_user_response = users_gateway_client.create_user()
print("Создан новый пользователь :", create_user_response)
print("=========================================================================== 01")

# Отправляем GET запрос на получение данных пользователя
get_user_response = users_gateway_client.get_user(create_user_response.user.id)
print("GET запрос на получение данных пользователя :", get_user_response)
print("=========================================================================== 02")
