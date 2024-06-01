from app.db.models.user import UserService, User, UserJSON
from app.repositories.user_repository import UserMySQL
import bcrypt


class UserDefault(UserService):
    def __init__(self, user_repository: UserMySQL):
        self.user_repository = user_repository

    def get_users(self) -> list[User]:
        return self.user_repository.get_users()

    def get_user_by_id(self, id: int) -> User:
        return self.user_repository.get_user_by_id(id)

    def get_user_by_username(self, username: str) -> User:
        return self.user_repository.get_user_by_username(username)

    def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_user_by_email(email)

    def create_user(self, user: UserJSON) -> User:
        # hash the password
        hashed_password = bcrypt.hashpw(
            user.password.encode('utf-8'), bcrypt.gensalt())
        user.password = hashed_password
        return self.user_repository.create_user(user)

    def update_user(self, user_id: int, user: User) -> User:
        return self.user_repository.update_user(user_id, user)