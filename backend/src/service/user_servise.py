from typing import List
from ..model.user_model import User
from ..core.types import UserType


class UserService:
    @staticmethod
    def create_user(data: UserType, current_user: UserType) -> UserType:
        if current_user.role != "admin":
            raise Exception("Permission denied")

        user = User.create(
            name=data.name,
            username=data.username,
            email=data.email,
            password_hash=data.password_hash,
            role=data.role,
            is_active=data.is_active,
        )

        return UserType(**user.__data__)

    @staticmethod
    def update_user(
        user_id: int,
        data: UserType,
        current_user: UserType,
    ) -> UserType:
        if current_user.role not in ["admin", "supervisor"]:
            raise Exception("Permission denied")

        user = User.select().where(User.id == user_id).first()

        user.name = data.name
        user.username = data.username
        user.email = data.email
        user.password_hash = data.password_hash
        user.role = data.role
        user.is_active = data.is_active

        user.save()
        return user

    @staticmethod
    def delete_user(user_id: int, current_user: UserType) -> None:
        if current_user.role != "admin":
            raise Exception("Permission denied")

        user = User.select().where(User.id == user_id).first()
        user.delete_instance()

    @staticmethod
    def get_user(user_id: int) -> UserType:
        user = User.select().where(User.id == user_id).first()
        return UserType(**user.__data__)

    @staticmethod
    def get_users() -> List[UserType]:
        users = User.select()
        return [UserType(**user.__data__) for user in users]
