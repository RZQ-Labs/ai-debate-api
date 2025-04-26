from sqlalchemy import Column, Integer, ForeignKey, Text
from . import Base

class Argument(Base):
    __tablename__ = "arguments"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    content = Column(Text)
    # Add more fields as needed
