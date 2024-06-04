from app.db.models.auction import Auction, AuctionService, AuctionJSON
from app.repositories.auction_repository import AuctionMySQL


class AuctionDefault(AuctionService):
    """Class for interacting with auction data in a default way."""

    def __init__(self, auction_repository: AuctionMySQL):
        """Initialize the AuctionDefault object.

        Args:
            auction_repository (AuctionRepository): An auction repository object.
        """
        self.auction_repository = auction_repository

    def get_auctions(self) -> list[Auction] | None:
        """Retrieve all auctions.

        Returns:
            List[Auction]: A list of auction objects.
        """
        return self.auction_repository.get_auctions()

    def get_auction_by_id(self, id: int) -> Auction | None:
        """Retrieve an auction by its ID.

        Args:
            id (int): The ID of the auction.

        Returns:
            Auction: The auction object.
        """
        return self.auction_repository.get_auction_by_id(id)

    def get_auctions_by_user_id(self, user_id: int) -> list[Auction] | None:
        """Retrieve all auctions for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            List[Auction]: A list of auction objects.
        """
        return self.auction_repository.get_auctions_by_user_id(user_id)

    def create_auction(self, auction: AuctionJSON) -> Auction | None:
        """Create a new auction.

        Args:
            user_id (int): The ID of the user.
            initial_amount (float): The initial amount of the auction.
            duration (int): The duration of the auction.
            state (str): The state of the auction.

        Returns:
            Auction: The auction object.
        """
        return self.auction_repository.create_auction(auction)

    def update_auction(self, id: int, state: str) -> Auction | None:
        """Update an auction.

        Args:
            auction (Auction): The auction object.

        Returns:
            Auction: The updated auction object.
        """
        return self.auction_repository.update_auction(id, state)
