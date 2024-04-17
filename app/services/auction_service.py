from app.db.models.auction import Auction, AuctionService


class AuctionDefault(AuctionService):
    """Class for interacting with auction data in a default way."""

    def __init__(self, auction_repository):
        """Initialize the AuctionDefault object.

        Args:
            auction_repository (AuctionRepository): An auction repository object.
        """
        self.auction_repository = auction_repository

    def get_auctions(self):
        """Retrieve all auctions.

        Returns:
            List[Auction]: A list of auction objects.
        """
        return self.auction_repository.get_auctions()

    def get_auction_by_id(self, id):
        """Retrieve an auction by its ID.

        Args:
            id (int): The ID of the auction.

        Returns:
            Auction: The auction object.
        """
        return self.auction_repository.get_auction_by_id(id)

    def get_auctions_by_user_id(self, user_id):
        """Retrieve all auctions for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            List[Auction]: A list of auction objects.
        """
        return self.auction_repository.get_auctions_by_user_id(user_id)
