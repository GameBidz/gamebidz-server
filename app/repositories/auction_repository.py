from app.db.models.auction import Auction, AuctionRepository, State, AuctionJSON
from datetime import datetime
import pymysql


class AuctionMySQL(AuctionRepository):
    """
    Represents a MySQL implementation of the AuctionRepository interface.
    """

    def __init__(self, connection: pymysql.Connection):
        """
        Initializes a new instance of the AuctionMySQL class.

        Args:
            connection (pymysql.Connection): The MySQL database connection.
        """
        self.connection = connection

    def get_auctions(self):
        """
        Retrieves all auctions from the database.

        Returns:
            list: A list of Auction objects representing the retrieved auctions.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM auctions")
            return [Auction(*result) for result in cursor.fetchall()]

    def get_auction_by_id(self, id: int) -> Auction | None:
        """
        Retrieves an auction by its ID from the database.

        Args:
            id (int): The ID of the auction.

        Returns:
            Auction: The Auction object representing the retrieved auction, or None if not found.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM auctions WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:
                return Auction(*result)
            return None

    def get_auctions_by_user_id(self, user_id: int) -> list[Auction] | None:
        """
        Retrieves all auctions associated with a specific user from the database.
        Args:
            user_id (int): The ID of the user.

        Returns:
            list: A list of Auction objects representing the retrieved auctions.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM auctions WHERE user_id = %s", (user_id,))
            return [Auction(*result) for result in cursor.fetchall()]

    def create_auction(self, auction: AuctionJSON) -> Auction | None:
        """
        Creates a new auction in the database.

        Args:
            auction (Auction): The Auction object representing the auction to create.

        Returns:
            Auction: The Auction object representing the created auction.
        """

        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        last_id = 0


        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO auctions (user_id, initial_amount, duration, state, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)",
                           (auction.user_id, auction.initial_amount, auction.duration, State.ACTIVE.value, created_at, updated_at))
            self.connection.commit()
            last_id = cursor.lastrowid

        return self.get_auction_by_id(last_id)

    def update_auction(self, id: int, state: str) -> Auction | None:
        """
        Updates the state of an auction in the database.

        Args:
            id (int): The ID of the auction to update.
            state (str): The new state of the auction.

        Returns:
            Auction: The Auction object representing the updated auction.
        """

        updated_at = datetime.now()

        with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE auctions SET state = %s, updated_at = %s WHERE id = %s", (state, updated_at, id))
            self.connection.commit()
            return self.get_auction_by_id(id)

    def get_auctions_by_state(self, state: str) -> list[Auction] | None:
        """
        Retrieves all auctions with a specific state from the database.

        Args:
            state (str): The state of the auctions to retrieve.

        Returns:
            list: A list of Auction objects representing the retrieved auctions.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM auctions WHERE state = %s", (state,))
            return [Auction(*result) for result in cursor.fetchall()]

    def delete_auction(self, id: int) -> bool:
        """
        Deletes an auction from the database.

        Args:
            id (int): The ID of the auction to delete.

        Returns:
            bool: True if the auction was successfully deleted, False otherwise.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM auctions WHERE id = %s", (id,))
            self.connection.commit()
            return True