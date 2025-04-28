from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime, func, String, Enum
from . import Base
from sqlalchemy.orm import relationship

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(Text, nullable=False)
    started_at = Column(DateTime, default=func.now())
    ended_at = Column(DateTime, nullable=True)
    initiator = Column(String, nullable=True, default="user", comment="Who initiated the session. The value can be 'user' or 'ai'.")
    user = relationship("User", back_populates="sessions")
    arguments = relationship("Argument", back_populates="session")
