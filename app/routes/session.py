from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.session import Session as SessionModel
from ..schemas.session_schema import SessionCreate, Session as SessionSchema
from ..database import get_db
from ..utils.auth import get_current_user
from ..settings import settings
from jose import JWTError
from devtools import debug

router = APIRouter(
    prefix="/session",
    tags=["Session"]
)

@router.post("/start")
async def start_session(db: AsyncSession = Depends(get_db), _: str = Depends(get_current_user)):
    return await db.execute(select(SessionModel).where(SessionModel.user_id == _))
