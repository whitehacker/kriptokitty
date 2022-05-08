from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
user = APIRouter()


@user.get("/")
async def read_users():
    return conn.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_users_by_id(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def create_users(user: User):
    conn.execute(users.insert().values(
        email=user.email,
        encrypted_password=user.encrypted_password
    ))
    return conn.execute(users.select()).fetchall()
@user.put("/{id}")
async def update_users(id: int, user: User):
    conn.execute(users.update().values(
        email=user.email,
        encrypted_password=user.encrypted_password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

@user.delete("/{id}")
async def delete_user(id= int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()