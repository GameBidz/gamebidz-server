from abc import ABC, abstractmethod


class User():
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier of the user.
        username (str): The username of the user.
        password (str): The password of the user.
        email (str): The email address of the user.
    """

    def __init__(self, id: int, username: str, password: str, email: str):
        self.id = id
        self.username = username
        self.password = password
        self.email = email


# User Repository
class UserRepository(ABC):
    """Interface for interacting with user data in the database."""

    @abstractmethod
    def get_users(self):
        """Retrieve all users.

        Returns:
            List[User]: A list of user objects.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def get_user_by_id(self, id: int):
        """Retrieve a user by their ID.

        Args:
            id (int): The ID of the user.

        Returns:
            User: The user object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def get_user_by_username(self, username: str):
        """Retrieve a user by their username.

        Args:
            username (str): The username of the user.

        Returns:
            User: The user object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.

        Returns:
            User: The user object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def get_user_by_email(self, email: str):
        """Retrieve a user by their email.

        Args:
            email (str): The email of the user.

        Returns:
            User: The user object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def create_user(self, user: User):
        """Create a new user.

        Args:
            user (User): The user object to be created.

        Returns:
            User: The created user object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def update_user(self, user: User):
        """Update an existing user.

        Args:
            user (User): The user object to be updated.

        Returns:
            User: The updated user object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def delete_user(self, id: int):
        """Delete a user by their ID.

        Args:
            id (int): The ID of the user to be deleted.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

# User Service


class UserService(ABC):
    """
    Abstract base class for user service.
    """

    @abstractmethod
    def get_user_by_id(self, id: int):
        """
        Get a user by their ID.

        Args:
            id (int): The ID of the user.

        Returns:
            User: The user object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def get_user_by_username(self, username: str):
        """
        Get a user by their username.

        Args:
            username (str): The username of the user.

        Returns:
            User: The user object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def get_user_by_email(self, email: str):
        """
        Get a user by their email.

        Args:
            email (str): The email of the user.

        Returns:
            User: The user object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def create_user(self, user: User):
        """
        Create a new user.

        Args:
            user (User): The user object to create.

        Returns:
            User: The created user object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def update_user(self, user: User):
        """
        Update an existing user.

        Args:
            user (User): The user object to update.

        Returns:
            User: The updated user object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def delete_user(self, id: int):
        """
        Delete a user by their ID.

        Args:
            id (int): The ID of the user to delete.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass
