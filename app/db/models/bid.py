from abc import ABC, abstractmethod


class Bid():
    def __init__(self, id, auction_id, user_id, amount, duration, state, created_at):
        self.id = id
        self.auction_id = auction_id
        self.user_id = user_id
        self.amount = amount
        self.duration = duration
        self.state = state
        self.created_at = created_at

# bid repository


class BidRepository(ABC):
    """Interface for interacting with bid data in the database."""

    @abstractmethod
    def get_bid_by_id(self, id):
        """Retrieve a bid by its ID.

        Args:
            id (int): The ID of the bid.

        Returns:
            Bid: The bid object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def get_bids_by_auction_id(self, auction_id):
        """Retrieve all bids for an auction.

        Args:
            auction_id (int): The ID of the auction.

        Returns:
            List[Bid]: A list of bid objects.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def get_bids_by_user_id(self, user_id):
        """Retrieve all bids for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            List[Bid]: A list of bid objects.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def create_bid(self, auction_id, user_id, amount):
        """Create a new bid.

        Args:
            auction_id (int): The ID of the auction.
            user_id (int): The ID of the user.
            amount (float): The amount of the bid.

        Returns:
            Bid: The bid object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def update_bid(self, id, amount):
        """Update the amount of a bid.

        Args:
            id (int): The ID of the bid.
            amount (float): The new amount of the bid.

        Returns:
            Bid: The updated bid object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass
