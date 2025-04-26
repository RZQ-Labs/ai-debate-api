from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from . import Base
from sqlalchemy.orm import relationship


class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    system_prompt = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    user = relationship("User", back_populates="prompts")
