from fastapi import Depends
from fastapi.security import HTTPBasic
from sqlmodel import Session

from app.api.deps import get_db
from app.core.security import verify_password
from app.models import User

security = HTTPBasic()


def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    if user := db.query(User).filter(User.username == username).first():
        return user if verify_password(password, user.hashed_password) else False
    else:
        return False
