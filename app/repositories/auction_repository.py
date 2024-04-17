from app.db.models.auction import Auction, AuctionRepository
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

    def get_auction_by_id(self, id: int):
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

    def get_auctions_by_user_id(self, user_id: int):
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

    def create_auction(self, user_id: int, initial_amount: float, duration: int):
        """
        Creates a new auction in the database.

        Args:
            user_id (int): The ID of the user creating the auction.
            initial_amount (float): The initial amount for the auction.
            duration (int): The duration of the auction in seconds.

        Returns:
            Auction: The Auction object representing the created auction.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO auctions (user_id, initial_amount, duration, state) VALUES (%s, %s, %s, 'active')",
                           (user_id, initial_amount, duration))
            self.connection.commit()
            return self.get_auction_by_id(cursor.lastrowid)

    def update_auction(self, id: int, state: str):
        """
        Updates the state of an auction in the database.

        Args:
            id (int): The ID of the auction to update.
            state (str): The new state of the auction.

        Returns:
            Auction: The Auction object representing the updated auction.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE auctions SET state = %s WHERE id = %s", (state, id))
            self.connection.commit()
            return self.get_auction_by_id(id)

    def get_auctions_by_state(self, state: str):
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

    def delete_auction(self, id: int):
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
