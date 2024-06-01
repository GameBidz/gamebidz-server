from fastapi import APIRouter, Response, status
from app.controllers.auction_controller import AuctionController
from app.services.auction_service import AuctionDefault
from app.repositories.auction_repository import AuctionMySQL
from app.db.db import connection


# Create a new instance of the AuctionMySQL class.
auction_repository = AuctionMySQL(connection)
# Create a new instance of the AuctionDefault class.
auction_service = AuctionDefault(auction_repository)
# Create a new instance of the AuctionController class.
auction_controller = AuctionController(auction_service)

# Define the router for the auction routes.
router = APIRouter()


# Define the route for retrieving all auctions.
@router.get("/auctions")
def get_auctions() -> dict:
    return {"auctions": auction_controller.get_auctions()}


# Define the route for retrieving an auction by its ID.
@router.get("/auctions/{auction_id}")
def get_auction_by_id(auction_id: int, response: Response) -> dict:
    auction = auction_controller.get_auction_by_id(auction_id)
    if not auction:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Auction not found"}
    return {"auction": auction}


# Define the route for retrieving all auctions for a user.
@router.get("/auctions/user/{user_id}")
def get_auctions_by_user_id(user_id: int) -> dict:
    return {"auctions": auction_controller.get_auctions_by_user_id(user_id)}


# Define the route for creating a new auction.
@router.post("/auctions")
def create_auction(auction: dict) -> dict:
    return {"auction": auction_controller.create_auction(auction)}


# Define the route for updating an auction.
@router.put("/auctions")
def update_auction(id: int, state: int) -> dict:
    return {"auction": auction_controller.update_auction(id, state)}
