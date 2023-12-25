from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserCreated(BaseModel):
    username: str
    email: EmailStr
