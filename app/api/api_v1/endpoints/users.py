from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import or_
from sqlalchemy.orm import Session
import app.crud.user as crud

from app.schemas.user import UserCreate, UserCreated
from app.api.deps import get_db
from app.models import User

router = APIRouter()


@router.post("/", response_model=UserCreated, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if (
        db_user := db.query(User)
        .filter(or_(User.email == user.email, User.username == user.username))
        .first()
    ):
        raise HTTPException(status_code=400, detail="Email or email already registered")
    return crud.create_user(db=db, user=user)
