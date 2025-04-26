from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class Log(BaseModel):
    id: int
    message: str
    level: str
    timestamp: datetime
