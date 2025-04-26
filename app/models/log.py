from sqlalchemy import Column, Integer, Text, String, DateTime, func
from . import Base

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text, nullable=False)
    level = Column(String, nullable=False)
    timestamp = Column(DateTime, default=func.now())
