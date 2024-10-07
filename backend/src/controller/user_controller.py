from fastapi import APIRouter
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

    data = (
        {"token": status_detail["data"]}
        if status_detail["data"]
        else {"error": status_detail["detail"]}
    )

    return JSONResponse(
        status_code=status_detail["status"],
        content=data,
    )
