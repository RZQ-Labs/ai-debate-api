from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class SessionBase(BaseModel):
    name: str

class SessionCreate(SessionBase):
    pass

class SessionClose(BaseModel):
    id: int

class Session(SessionBase):
    id: int
    user_id: int
    started_at: datetime
    ended_at: Optional[datetime]

    class Config:
        orm_mode = True
