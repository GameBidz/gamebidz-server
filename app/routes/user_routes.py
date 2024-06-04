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
def get_users(response: Response, email: str | None = None, username: str | None = None):
    if email:
        return {"users": hd.get_user_by_email(email, response)}
    if username:
        return {"users": hd.get_user_by_username(username, response)}
    return {"users": hd.get_users()}


# Define the route for retrieving a user by their ID.
@router.get("/users/{user}")
def get_user(user: int, response: Response):
    return hd.get_user_by_username(user, response)


# Define the route for creating a new user.
@router.post("/users")
def create_user(user: UserJSON, response: Response):
    return {"user": hd.create_user(user, response)}


# Define the route for updating a user.
@router.put("/users")
def update_user(user):
    return {"user": hd.update_user(user)}