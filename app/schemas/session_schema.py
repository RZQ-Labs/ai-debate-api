from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class SessionBase(BaseModel):
    name: str
    user_id: int
    started_at: datetime

class SessionCreate(SessionBase):
    pass

class Session(SessionBase):
    id: int
    ended_at: Optional[datetime]

    class Config:
        orm_mode = True
