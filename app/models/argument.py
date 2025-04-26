from sqlalchemy import Column, Integer, ForeignKey, Text, String, DateTime
from . import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class Argument(Base):
    __tablename__ = "arguments"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    content = Column(Text, nullable=False)
    by = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    session = relationship("Session", back_populates="arguments")
