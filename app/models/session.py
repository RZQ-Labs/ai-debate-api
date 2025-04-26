from sqlalchemy import Column, Integer, ForeignKey, DateTime
from . import Base

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    started_at = Column(DateTime)
    # Add more fields as needed
