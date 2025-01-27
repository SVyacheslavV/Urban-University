from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=15, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=100, description='Enter age')]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[str, Path(min_length=1, max_length=10, regex='[0-9]', description='Enter user_id')],
        username: Annotated[str, Path(min_length=5, max_length=15, description='Enter username')],
        age: Annotated[int, Path(ge=18, le=100, description='Enter age')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[
            str, Path(min_length=1, max_length=10, regex='[0-9]', description='Enter user_id')]) -> str:
    if user_id in users:
        del users[user_id]
        return f'User {user_id} has been deleted'

# uvicorn module_16.module_16_3:app
