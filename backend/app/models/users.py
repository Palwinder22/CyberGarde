# app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    company = Column(String(150))
    position = Column(String(100))
    license_key = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    
