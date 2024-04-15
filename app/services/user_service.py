from app.db.models.user import UserService, User
from app.repositories.user_repository import UserMySQL
import pymysql


class UserDefault(UserService):
    def __init__(self, connection: pymysql.Connection):
        self.connection = connection
        self.user_repository = UserMySQL(connection)

    def get_users(self):
        return self.user_repository.get_users()

    def get_user_by_id(self, id: int):
        return self.user_repository.get_user_by_id(id)

    def get_user_by_username(self, username: str):
        return self.user_repository.get_user_by_username(username)

    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email)

    def create_user(self, username: str, email: str, password: str):
        return self.user_repository.create_user(username, email, password)

    def update_user(self, user: User):
        return self.user_repository.update_user(user)

    def delete_user(self, id: int):
        return self.user_repository.delete_user(id)
