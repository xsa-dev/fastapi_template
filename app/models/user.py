from sqlalchemy import Column, Integer, String
from app.database import Base
from app.security.password_handling import get_hashed_password

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    def set_password(self, password: str):
        self.hashed_password = get_hashed_password(password)
