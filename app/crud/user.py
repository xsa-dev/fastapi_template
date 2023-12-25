from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash, verify_password, get_user_by_username


def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.__dict__


def authenticate_user(db: Session, username: str, password: str):
    if user := get_user_by_username(db, username):
        return user if verify_password(password, user.hashed_password) else False
    else:
        return False
