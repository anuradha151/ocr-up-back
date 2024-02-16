from sqlalchemy import Column , Integer, String, DateTime
from config.db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)