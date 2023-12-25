from fastapi import APIRouter
from app.api.api_v1.endpoints import users, login, notes

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(login.router, tags=["login"])
api_router.include_router(notes.router, prefix="/notes", tags=["notes"])
