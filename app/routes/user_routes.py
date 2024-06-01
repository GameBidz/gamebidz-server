from fastapi import APIRouter, Response, status
from app.db.models.user import UserJSON
from app.controllers.user_controller import UserController
from app.services.user_service import UserDefault
from app.repositories.user_repository import UserMySQL
from app.db.db import connection

# Create a new instance of the UserMySQL class.
rp = UserMySQL(connection)
# Create a new instance of the UserDefault class.
sv = UserDefault(rp)
# Create a new instance of the UserController class.
hd = UserController(sv)

# Define the router for the user routes.
router = APIRouter()


# Define the route for retrieving all users.
@router.get("/users")
def get_users():
    return {"users": hd.get_users()}


# Define the route for retrieving a user by their ID.
@router.get("/users/{user_id}")
def get_user_by_id(user_id: int, response: Response):
    user = hd.get_user_by_id(user_id)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "User not found"}
    return {"user": hd.get_user_by_id(user_id)}


# Define the route for retrieving a user by their username.
@router.get("/users/{username}")
def get_user_by_username(username: str, response: Response):
    user = hd.get_user_by_username(username)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "User not found"}
    return {"user": hd.get_user_by_username(username)}


# Define the route for retrieving a user by their email.
@router.get("/users/{email}")
def get_user_by_email(email: str, response: Response):
    user = hd.get_user_by_email(email)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "User not found"}
    return {"user": hd.get_user_by_email(email)}


# Define the route for creating a new user.
@router.post("/users")
def create_user(username: str, email: str, password: str):
    return {"user": hd.create_user(username, email, password)}


# Define the route for updating a user.
@router.put("/users")
def update_user(user):
    return {"user": hd.update_user(user)}


# Define the route for deleting a user.
@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"user": hd.delete_user(user_id)}
