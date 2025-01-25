from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def enter_main() -> str:
    return f'Главная страница'


# Запрос: http://127.0.0.1:8080/
# Ответ: "Главная страница"


@app.get('/user/admin')
async def enter_admin() -> str:
    return 'Вы вошли как администратор'


# Запрос: http://127.0.0.1:8080/user/admin
# Ответ: "Вы вошли как администратор"


@app.get('/user/{user_id}')
async def enter_user_id(user_id: int) -> str:
    return f'Вы вошли как пользователь № {user_id}'


# Запрос: http://127.0.0.1:8080/user/12345
# Ответ: "Вы вошли как пользователь № 12345"


@app.get('/user')
async def get_user(username: str, age: int) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
# Запрос: http://127.0.0.1:8080/user?username=%27Slava%27&age=35
# Ответ: "Информация о пользователе. Имя: 'Slava', Возраст: 35"


# uvicorn module_16.module_16_1:app
