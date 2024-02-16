from typing import Annotated
from fastapi import Depends, FastAPI,File, UploadFile;
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel;
from ml_txt_detection import detect
# from routes.user import user
import models
from config.db import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()
# app.include_router(user) 

models.Base.metadata.create_all(bind=engine)


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():    
    return {"Hellow": "World"}

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile=File(...)):
    reponse = detect(file.file)    
    return {
        "text":reponse
    }

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)

@app.post("/user") 
async def create_user(user: UserBase, db: Session = db_dependency):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()

@app.get("/users")
async def read_data(db: Session = db_dependency):
    return db.query(models.User).all()

@app.get("/user/{id}")
async def read_data(id: int, db: Session = db_dependency):
    return db.query(models.User).filter(models.User.id == id).first()   

