from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from pydantic import BaseModel

# state enum
class State(Enum):
    ACTIVE = 'active'
    FINISHED = 'finished'
    CANCELED = 'canceled'

class AuctionJSON(BaseModel):
    """
    Represents an auction request.

    Attributes:
        user_id (int): The ID of the user who published the auction.
        initial_amount (float): The initial amount of the auction.
        duration (int): The duration of the auction in minutes.
    """

    user_id: int
    initial_amount: int
    duration: int

class Auction():
    """
    Represents an auction.

    Attributes:
        id (int): The unique identifier of the auction.
        user_id (int): The identifier of the user who published the auction.
        initial_amount (float): The amount of the auction.
        duration (int): The duration of the auction in minutes.
        state (str): The state of the auction (active, finished, canceled).
        created_at (datetime): The timestamp when the auction was created.
    """

    def __init__(self, id: int, user_id: int, initial_amount: int, duration: int, state: str, created_at: datetime, updated_at: datetime):
        self.id = id
        self.user_id = user_id
        self.initial_amount = initial_amount
        self.duration = duration
        self.state = state
        self.created_at = created_at
        self.updated_at = updated_at

class AuctionRepository(ABC):
    """Interface for interacting with auction data in the database."""

    @abstractmethod
    def get_auctions(self) -> list[Auction] | None:
        """Retrieve all auctions.

        Returns:
            List[Auction]: A list of auction objects.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def get_auction_by_id(self, id: int) -> Auction | None:
        """Retrieve an auction by its ID.

        Args:
            id (int): The ID of the auction.

        Returns:
            Auction: The auction object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def get_auctions_by_user_id(self, user_id: int) -> list[Auction] | None:
        """Retrieve all auctions for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            List[Auction]: A list of auction objects.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def create_auction(self, auction: AuctionJSON) -> Auction | None:
        """Create a new auction.

        Args:
            user_id (int): The ID of the user.
            initial_amount (int): The initial amount of the auction.
            duration (int): The duration of the auction in minutes.

        Returns:
            Auction: The auction object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def update_auction(self, id: int, state: str) -> Auction | None:
        """Update the initial amount of an auction.

        Args:
            id (int): The ID of the auction.
            initial_amount (float): The new initial amount of the auction.
            state (str): The state of the auction.
            
        Returns:
            Auction: The updated auction object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

class AuctionService(ABC):
    """Interface for interacting with auctions repository."""

    @abstractmethod
    def get_auctions(self) -> list[Auction] | None:
        """Retrieve all auctions.

        Returns:
            List[Auction]: A list of auction objects.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def get_auction_by_id(self, id: int) -> Auction | None:
        """Retrieve an auction by its ID.

        Args:
            id (int): The ID of the auction.

        Returns:
            Auction: The auction object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def get_auctions_by_user_id(self, user_id: int) -> list[Auction] | None:
        """Retrieve all auctions for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            List[Auction]: A list of auction objects.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def create_auction(self, auction: Auction) -> Auction | None:
        """Create a new auction.

        Args:
            user_id (int): The ID of the user.
            initial_amount (int): The initial amount of the auction.
            duration (int): The duration of the auction in minutes.

        Returns:
            Auction: The auction object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def update_auction(self, id: int, state: str) -> Auction | None:
        """Update the initial amount of an auction.

        Args:
            id (int): The ID of the auction.
            initial_amount (float): The new initial amount of the auction.

        Returns:
            Auction: The updated auction object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass
