# pip install Faker

from faker import Faker

fake = Faker('ru_RU')

user_data = {
    "name": fake.name(),
    "email": fake.email(domain="yandex.ru"),
    "address": fake.address()
}


print(fake.name())
print(fake.address())
print(fake.email())
print(fake.email(domain="yandex.ru"))
print(user_data)