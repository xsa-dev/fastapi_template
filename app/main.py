from fastapi import FastAPI
from app.api.api_v1.api import api_router

app = FastAPI()
app.include_router(api_router, prefix='/api/v1')


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI server!"}
