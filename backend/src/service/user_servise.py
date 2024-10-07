from typing import List
from ..model.user_model import User
from ..core.types import UserType
from ..core.security import Security
from ..utils.status import get_status_detail, StatusDetail


class UserService:
    @staticmethod
    def login(
        username_or_email: str,
        password: str,
    ) -> StatusDetail[str | None]:
        user = (
            User.select()
            .where(
                (User.username == username_or_email)
                | (User.email == username_or_email,)
            )
            .first()
        )

        if not user or not Security.verify_password(
            password,
            user.password_hash,
        ):
            return get_status_detail(401)

        token = Security.create_jwt({"sub": user.id})
        return get_status_detail(200, token)

    @staticmethod
    def create_user(
        data: UserType,
        current_user: UserType,
    ) -> StatusDetail[UserType | None]:
        if current_user.role != "admin":
            return get_status_detail(403)

        user = User.create(
            name=data.name,
            username=data.username,
            email=data.email,
            password_hash=Security.hash_password(data.password),
            role=data.role,
            is_active=data.is_active,
        )

        return get_status_detail(201, UserType(**user.__data__))

    @staticmethod
    def update_user(
        user_id: int,
        data: UserType,
        current_user: UserType,
    ) -> StatusDetail[UserType | None]:
        if current_user.role not in ["admin", "supervisor"]:
            return get_status_detail(403)

        user = User.select().where(User.id == user_id).first()
        if not user:
            return get_status_detail(404)

        user.name = data.name
        user.username = data.username
        user.email = data.email
        user.password_hash = Security.hash_password(data.password)
        user.role = data.role
        user.is_active = data.is_active

        user.save()
        return get_status_detail(200, UserType(**user.__data__))

    @staticmethod
    def delete_user(user_id: int, current_user: UserType) -> StatusDetail:
        if current_user.role != "admin":
            return get_status_detail(403)
        user = User.select().where(User.id == user_id).first()
        if user:
            user.delete_instance()
            return get_status_detail(204)
        else:
            return get_status_detail(404)

    @staticmethod
    def get_user(user_id: int) -> StatusDetail[UserType | None]:
        user = User.select().where(User.id == user_id).first()
        if not user:
            return get_status_detail(404)
        return get_status_detail(200, UserType(**user.__data__))

    @staticmethod
    def get_users() -> StatusDetail[List[UserType]]:
        users = User.select()
        data = [UserType(**user.__data__) for user in users]
        return get_status_detail(200, data)
