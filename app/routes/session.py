from devtools import debug
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models.session import Session as SessionModel
from ..models.user import User
from ..schemas.session_schema import SessionCreate, Session as SessionSchema
from ..database import get_db
from ..utils.auth import get_current_user
from datetime import datetime
import traceback

router = APIRouter(
    prefix="/session",
    tags=["Session"]
)

@router.post("/start", response_model=SessionSchema)
async def start_session(session: SessionCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        # Validate session data
        if not session.name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Session name is required"
            )

        # Create a new session model instance
        new_session = SessionModel(
            name=session.name,
            user_id=current_user.id,
            started_at=datetime.now()
        )

        # Add to database and commit
        db.add(new_session)
        await db.commit()
        await db.refresh(new_session)

        # Return the created session
        return new_session
    except Exception as e:
        traceback.print_exc()
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create session: {str(e)}"
        )

@router.post("/end", response_model=SessionSchema, status_code=status.HTTP_200_OK)
async def end_session(session_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        # Find the session by ID
        result = await db.execute(select(SessionModel).where(SessionModel.id == session_id))
        session = result.scalars().first()
        if not session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Session not found"
            )

        # Update session end time
        session.ended_at = datetime.now()
        await db.commit()
        await db.refresh(session)

        # Return the updated session
        return session
    except Exception as e:
        traceback.print_exc()
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to end session: {str(e)}"
        )
