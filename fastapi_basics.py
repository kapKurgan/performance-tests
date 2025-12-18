# uvicorn fastapi_basics:app_12345 --reload

# Импортируем основной класс FastAPI из библиотеки fastapi
from fastapi import FastAPI, Query, Path, Body, APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
import uvicorn

# Создаем объект приложения FastAPI
# Параметр title задает название нашего приложения, которое будет отображаться в документации
app_12345 = FastAPI(title="my_basics")

router_123 = APIRouter(
    prefix="/api/v1",
    tags=["MyBasics1"]
)


# Pydantic-модель для описания структуры пользователя
class User(BaseModel):
    username: str  # логин пользователя
    email: str     # email пользователя
    age: int       # возраст пользователя


# Модель ответа
class UserResponse(BaseModel):
    username: str
    email: str
    message: str


# Зависимость: проверка минимального возраста
def validate_min_age(min_age: int = 18):
    def checker(user: User):
        if user.age < min_age:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User must be at least {min_age} years old"
            )
        return user

    return checker


# базовый GET-эндпоинт по пути /api/v1/basics
@router_123.get("/basics/{item_id_12345}")
async def get_basics(
    name: str = Query("Alise", description="Имя пользователя"),
    item_id_12345: int = Path(..., description="Идентификатор элемента")
):
    # возвращаем простой JSON с сообщением
    return {"message": f"Hello, {name}!",
            "description": f"Item number {item_id_12345}"
    }


# POST-эндпоинт для создания пользователя
@router_123.post("/basics/user", response_model=UserResponse)
async def create_user(user: User = Body(..., description="Данные нового пользователя")) -> UserResponse:
    # FastAPI автоматически:
    # 1) распарсит JSON из тела запроса
    # 2) провалидирует его по полям модели User
    return UserResponse(
        username=user.username,
        email=user.email,
        age=user.age,
        message="User created successfully!"
    )


# Эндпоинт использует Depends для валидации возраста
@router_123.post("/basics/register", summary="Регистрация пользователя с проверкой возраста")
async def register_user(
        user: User = Depends(validate_min_age(min_age=21))  # внедряем зависимость
):
    return {
        "message": f"User {user.username} registered successfully",
        "email": user.email,
        "age": user.age
    }


app_12345.include_router(router_123)

# --------------------------------------------------------
# Программный запуск приложения
# --------------------------------------------------------
if __name__ == "__main__":
    # Запускаем Uvicorn с указанием:
    # - имя модуля и объекта приложения (fastapi_basics:app)
    # - адрес и порт (host, port)
    # - авто-перезагрузка при изменении кода (reload=True)
    uvicorn.run(
        "fastapi_basics:app_12345",  # "<module_name>:<app_instance>"
        host="127.0.0.1",  # адрес, на котором слушаем входящие подключения
        port=8010,  # порт
        reload=True,  # перезагрузка при изменении файлов
        log_level="info"  # уровень логирования
    )


