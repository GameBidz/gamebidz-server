from app.db.models.user import User
from app.services.user_service import UserDefault
import pymysql


class UserController():
    def __init__(self, connection: pymysql.Connection):
        self.user_service = UserDefault(connection)

    def get_users(self):
        return self.user_service.get_users()

    def get_user_by_id(self, id: int):
        return self.user_service.get_user_by_id(id)

    def get_user_by_username(self, username: str):
        return self.user_service.get_user_by_username(username)

    def get_user_by_email(self, email: str):
        return self.user_service.get_user_by_email(email)

    def create_user(self, username: str, email: str, password: str):
        return self.user_service.create_user(username, email, password)

    def update_user(self, user: User):
        return self.user_service.update_user(user)

    def delete_user(self, id: int):
        return self.user_service.delete_user(id)
