# pip install 'pydantic[email]'

from pydantic import BaseModel


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = False


user = User(id=1, name="Алиса", email="alise@yandex.ru", address={"city": "Moscow", "zip_code": "125000"})
user1 = User(id=1, name="Алиса", email="alise@yandex.ru", address=Address(city="Moscow", zip_code="125000"))
print(user)
print(user.email)
print(user1.address.city)






















