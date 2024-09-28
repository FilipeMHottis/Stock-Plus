from fastapi import FastAPI
from .startup import create_db

app = FastAPI(lifespan=create_db)


@app.get("/")
async def root():
    return {"message": "Hello World"}
