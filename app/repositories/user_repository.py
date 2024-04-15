from app.db.models.user import User, UserRepository
import pymysql

# path: gamebidz-server/app/repositories/user-mysql.py


class UserMySQL(UserRepository):
    """Class for interacting with user data in a MySQL database."""

    def __init__(self, connection: pymysql.Connection):
        """Initialize the UserMySQL object.

        Args:
            connection (pymysql.Connection): A connection to the MySQL database.
        """
        self.connection = connection

    def get_users(self):
        """Retrieve all users.

        Returns:
            List[User]: A list of user objects.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            return [User(*result) for result in cursor.fetchall()]

    def get_user_by_id(self, id: int):
        """Retrieve a user by their ID.

        Args:
            id (int): The ID of the user.

        Returns:
            User: The user object.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:
                return User(*result)
            return None

    def get_user_by_username(self, username: str):
        """Retrieve a user by their username.

        Args:
            username (str): The username of the user.

        Returns:
            User: The user object.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            if result:
                return User(*result)
            return None

    def get_user_by_email(self, email: str):
        """Retrieve a user by their email.

        Args:
            email (str): The email of the user.

        Returns:
            User: The user object.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            result = cursor.fetchone()
            if result:
                return User(*result)
            return None

    def create_user(self, username: str, password: str, email: str):
        """Create a new user.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
            email (str): The email of the user.

        Returns:
            User: The user object.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                (username, password, email)
            )
            self.connection.commit()
            return User(cursor.lastrowid, username, password, email)

    def update_user(self, user: User):
        """Update a user.

        Args:
            user (User): The user object to be updated.

        Returns:
            User: The updated user object.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE users SET username = %s, password = %s, email = %s WHERE id = %s",
                (user.username, user.password, user.email, user.id)
            )
            self.connection.commit()
            return user

    def delete_user(self, id: int):
        """Delete a user.

        Args:
            id (int): The ID of the user.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s", (id,))
            self.connection.commit()
