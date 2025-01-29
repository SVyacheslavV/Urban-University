from fastapi import FastAPI, HTTPException, Request, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates
from typing import List, Annotated

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


class UserCreate(BaseModel):
    username: str = Field(..., min_length=5, max_length=15, description='Enter username')
    age: int = Field(..., ge=18, le=100, description='Enter age')


@app.get('/', response_class=HTMLResponse)
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/user/{user_id}', response_class=HTMLResponse)
def get_user(request: Request, user_id: int) -> HTMLResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail='User not found')


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
async def delete_user(user_id: int):
    for i, t in enumerate(users):
        if t.id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail='User was not found')

# uvicorn module_16_5:app
