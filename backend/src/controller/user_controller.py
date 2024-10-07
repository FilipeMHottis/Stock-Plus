from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ..service.user_servise import UserService
from pydantic import BaseModel

router = APIRouter()


class Login(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(login: Login):
    status_detail = UserService.login(login.username, login.password)

    if status_detail["status"] != 200:
        raise HTTPException(
            status_code=status_detail["status"],
            detail=status_detail["detail"],
        )

    return JSONResponse(
        status_code=status_detail["status"],
        content={"token": status_detail["data"]},
    )
