from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class SessionBase(BaseModel):
    pass

class SessionCreate(SessionBase):
    pass

class Session(SessionBase):
    id: int
    user_id: int
    started_at: datetime
    ended_at: Optional[datetime]
    class Config:
        orm_mode = True

class ArgumentBase(BaseModel):
    content: str

class ArgumentCreate(ArgumentBase):
    pass

class Argument(ArgumentBase):
    id: int
    session_id: int
    created_at: datetime
    class Config:
        orm_mode = True

class Log(BaseModel):
    id: int
    message: str
    level: str
    timestamp: datetime
    class Config:
        orm_mode = True
