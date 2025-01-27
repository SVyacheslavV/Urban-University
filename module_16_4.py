from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


class UserCreate(BaseModel):
    username: str = Field(..., min_length=5, max_length=15, description='Enter username')
    age: int = Field(..., ge=18, le=100, description='Enter age')


@app.get('/users', response_model=List[User])
async def get_all_users():
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def create_user(user: UserCreate):
    new_id = len(users) + 1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: int, user: UserCreate):
    for t in users:
        if t.id == user_id:
            t.username = user.username
            t.age = user.age
            return t
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}', response_model=User)
async def delete_task(user_id: int):
    for i, t in enumerate(users):
        if t.id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail='User was not found')

# uvicorn module_16.module_16_4:app
