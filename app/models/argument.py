from sqlalchemy import Column, Integer, ForeignKey, Text, String, DateTime
from . import Base
from datetime import datetime, timezone

class Argument(Base):
    __tablename__ = "arguments"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    content = Column(Text)
    by = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    # Add more fields as needed
