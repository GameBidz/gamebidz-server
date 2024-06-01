from app.services.auction_service import AuctionService
from app.db.models.auction import Auction


class AuctionController:
    """Class for interacting with auctions."""

    def __init__(self, auction_service: AuctionService):
        """Initialize the AuctionController object.

        Args:
            auction_service (AuctionService): An auction service object.
        """
        self.auction_service = auction_service

    def get_auctions(self) -> list[Auction] | None:
        """Retrieve all auctions.

        Returns:
            List[Auction]: A list of auction objects.
        """
        return self.auction_service.get_auctions()

    def get_auction_by_id(self, id: int) -> Auction | None:
        """Retrieve an auction by its ID.

        Args:
            id (int): The ID of the auction.

        Returns:
            Auction: The auction object.
        """
        return self.auction_service.get_auction_by_id(id)

    def get_auctions_by_user_id(self, user_id: int) -> list[Auction] | None:
        """Retrieve all auctions for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            List[Auction]: A list of auction objects.
        """
        return self.auction_service.get_auctions_by_user_id(user_id)
    
    def create_auction(self, auction: Auction) -> Auction | None:
        """Create a new auction.

        Args:
            user_id (int): The ID of the user.
            initial_amount (float): The initial amount of the auction.
            duration (int): The duration of the auction.
            state (str): The state of the auction.

        Returns:
            Auction: The auction object.
        """
        return self.auction_service.create_auction(auction)
    
    def update_auction(self, id: int, state: str) -> Auction | None:
        """Update an auction.

        Args:
            id (int): The ID of the auction.
            state (str): The state of the auction.

        Returns:
            Auction: The updated auction object.
        """
        return self.auction_service.update_auction(id, state)
