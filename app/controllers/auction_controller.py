from app.services.auction_service import AuctionService


class AuctionController:
    """Class for interacting with auctions."""

    def __init__(self, auction_service: AuctionService):
        """Initialize the AuctionController object.

        Args:
            auction_service (AuctionService): An auction service object.
        """
        self.auction_service = auction_service

    def get_auctions(self):
        """Retrieve all auctions.

        Returns:
            List[Auction]: A list of auction objects.
        """
        return self.auction_service.get_auctions()

    def get_auction_by_id(self, id):
        """Retrieve an auction by its ID.

        Args:
            id (int): The ID of the auction.

        Returns:
            Auction: The auction object.
        """
        return self.auction_service.get_auction_by_id(id)

    def get_auctions_by_user_id(self, user_id):
        """Retrieve all auctions for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            List[Auction]: A list of auction objects.
        """
        return self.auction_service.get_auctions_by_user_id(user_id)
