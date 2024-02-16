# from fastapi import APIRouter
# from config.db import conn
# from models import users

# user =  APIRouter()

# @user.get("/")
# async def read_data():
#     return conn.execute(users.select()).fetchall()

# @user.get("/{id}")
# async def read_data(id: int):
#     return conn.execute(users.select().where(users.c.id == id)).fetchall()

# @user.post("/") 
# async def create_user(user: User):
#     conn.execute(users.insert().values(
#         first_name=user.first_name,
#         last_name=user.last_name,
#         email=user.email,
#         password=user.password
#     ))
#     return {"message": "User has been created successfully."}