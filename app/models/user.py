from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from . import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # Add more fields as needed
