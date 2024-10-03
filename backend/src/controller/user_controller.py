from ..service.user_servise import UserService  # Corrigido o nome do serviço
from ..core.types import UserType
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/users")
def get_users():
    try:
        users = (
            UserService.get_users()
        )
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/users/{user_id}")
def get_user(user_id: int):
    try:
        user = UserService.get_user(
            user_id
        )
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
