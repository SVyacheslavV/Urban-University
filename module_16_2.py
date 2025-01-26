from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get('/user/{user_id}')
# async def enter_user_id(user_id: Annotated[int, Path(gt=0, le=100, description='Enter User ID')]) -> str:
async def enter_user_id(user_id: int = Path(gt=0, le=100, description='Enter User ID')) -> str: # без Annotated
    return f'Вы вошли как пользователь № {user_id}'

# Запрос: http://127.0.0.1:8000/user/1
# Ответ: "Вы вошли как пользователь № 1"

# Запрос: http://127.0.0.1:8000/user/101
# Ответ:
# {
#   "detail": [
#     {
#       "type": "less_than_equal",
#       "loc": [
#         "path",
#         "user_id"
#       ],
#       "msg": "Input should be less than or equal to 100",
#       "input": "101",
#       "ctx": {
#         "le": 100
#       }
#     }
#   ]
# }

@app.get('/user/{username}/{age}')
async def get_user(username: Annotated[str, Path(min_length=5, max_length=20,description='Enter username')],
                   age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

# Запрос: http://127.0.0.1:8000/user/Dimas/36
# Ответ: "Информация о пользователе. Имя: Dimas, Возраст: 36"

# Запрос: http://127.0.0.1:8000/user/Dim/36
# Ответ:
# {
#   "detail": [
#     {
#       "type": "string_too_short",
#       "loc": [
#         "path",
#         "username"
#       ],
#       "msg": "String should have at least 5 characters",
#       "input": "Dim",
#       "ctx": {
#         "min_length": 5
#       }
#     }
#   ]
# }

# Запрос: http://127.0.0.1:8000/user/Dimon/15
# Ответ:
# {
#   "detail": [
#     {
#       "type": "greater_than_equal",
#       "loc": [
#         "path",
#         "age"
#       ],
#       "msg": "Input should be greater than or equal to 18",
#       "input": "15",
#       "ctx": {
#         "ge": 18
#       }
#     }
#   ]
# }


# uvicorn module_16.module_16_2:app