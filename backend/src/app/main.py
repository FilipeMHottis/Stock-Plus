from fastapi import FastAPI
from .startup import create_db

from ..controller.user_controller import router as user_router

app = FastAPI(lifespan=create_db)

app.include_router(user_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Hello World"}
