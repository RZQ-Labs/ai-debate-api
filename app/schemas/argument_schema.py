from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


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
