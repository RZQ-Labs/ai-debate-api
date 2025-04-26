from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime, timezone
from . import Base

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    started_at = Column(DateTime, default=datetime.now(timezone.utc))
    ended_at = Column(DateTime, nullable=True)
    # Add more fields as needed
