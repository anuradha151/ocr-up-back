from fastapi import APIRouter, Depends
from models.User import UserBase
import schemas
from sqlalchemy.orm import Session
from config.db import SessionLocal

user =  APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)

@user.post("/") 
async def create_user(user: UserBase, db: Session = db_dependency):
    db_user = schemas.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    return {"message": "User has been created successfully"}

@user.get("/")
async def read_data(db: Session = db_dependency):
    return db.query(schemas.User).all()

@user.get("/{id}")
async def read_data(id: int, db: Session = db_dependency):
    return db.query(schemas.User).filter(schemas.User.id == id).first() 