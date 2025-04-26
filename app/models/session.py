from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime, timezone
from . import Base
from sqlalchemy.orm import relationship

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    started_at = Column(DateTime, default=datetime.now(timezone.utc))
    ended_at = Column(DateTime, nullable=True)
    user = relationship("User", back_populates="sessions")
    arguments = relationship("Argument", back_populates="session")
