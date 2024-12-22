from fastapi import FastAPI
from typing import List
from uuid import UUID, uuid4
from models import *

"""
main.py
This module contains the FastAPI application for myapp.
Functions:
    read_root: A simple endpoint that returns a greeting message.
"""

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("52cd088a-ad00-4d35-812e-24f6693afea6"),
        first_name="John",
        last_name="Doe",
        middle_name="Smith",
        gender=Gender.male,
        roles=[Role.student]

    ),
    User(
        id=UUID("711644e6-79c9-4dae-9214-d4770dd514a6"),
        first_name="Jane",
        last_name="Smith",
        middle_name="Doe",
        gender=Gender.female,
        roles=[Role.student]

    )
]


@app.get("/api/users")
async def users():
    return db

@app.get("/api/users/{user_id}")
async def user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    return {"message": "User not found"}

@app.post("/api/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.get("/")
def root():
    return {"Hello": "Kib"}
