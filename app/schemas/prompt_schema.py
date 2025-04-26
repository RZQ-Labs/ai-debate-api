from pydantic import BaseModel, Field
from datetime import datetime

class PromptBase(BaseModel):
    system_prompt: str
    max_tokens: int = Field(1024, description="Maximum tokens to generate.", gt=0)

class PromptInput(BaseModel):
    prompt: str

class Prompt(PromptBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
