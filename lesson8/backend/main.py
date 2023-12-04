from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr
from typing import List, Optional

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы
    allow_headers=["*"],  # Разрешает все заголовки
)

class UserBase(BaseModel):
    name: constr(min_length=4, max_length=20)
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

users: List[User] = []

@app.get("/")
def get_main_page():
    return {"message": "Hello world"}

@app.get("/users", response_model=List[User])
def get_users():
    return users

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=User, status_code=500)
def create_user(user_data: UserCreate):
    new_user_id = len(users) + 1  # Генерируем новый ID
    new_user = User(id=new_user_id, **user_data.dict())  # Создаем объект User
    users.append(new_user)
    return new_user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, update_data: User):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = update_data.name
    user.email = update_data.email
    return user

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    users.remove(user)
    return