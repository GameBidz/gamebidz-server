from app.db.models.user import UserJSON, User
from app.services.user_service import UserDefault
from fastapi import Response, status


class UserController():
    def __init__(self, user_service: UserDefault):
        self.user_service = user_service

    def get_users(self) -> list[User]:
        return self.user_service.get_users()

    def get_user_by_id(self, id: int, response: Response) -> dict[str, str] | User:
        user = self.user_service.get_user_by_id(id)
        if not user:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "User not found"}
        return user

    def get_user_by_username(self, username: str, response: Response) -> dict[str, str]:
        user = self.user_service.get_user_by_username(username)
        if not user:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "User not found"}
        return {"user": user}

    def get_user_by_email(self, email: str, response: Response) -> dict[str, str]:
        user = self.user_service.get_user_by_email(email)
        if not user:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "User not found"}
        return {"user": user}

    def create_user(self, user: UserJSON, response: Response) -> dict[str, str] | User:
        find_user = self.get_user_by_username(user.username, response)
        if find_user.get("user"):
            response.status_code = status.HTTP_409_CONFLICT
            return {"error": "Username already exists"}
        find_user = self.get_user_by_email(user.email, response)
        if find_user.get("user"):
            response.status_code = status.HTTP_409_CONFLICT
            return {"error": "Email already exists"}
        response.status_code = status.HTTP_201_CREATED
        return self.user_service.create_user(user)

    def update_user(self, user_id: int, user: UserJSON) -> User:
        return self.user_service.update_user(user_id, user)
