from fastapi import APIRouter, Response, status
from app.db.models.user import UserJSON
from app.controllers.user_controller import UserController
from app.services.user_service import UserDefault
from app.repositories.user_repository import UserMySQL
from app.db.db import connection

# Create a new instance of the UserMySQL class.
user_repository = UserMySQL(connection)
# Create a new instance of the UserDefault class.
user_service = UserDefault(user_repository)
# Create a new instance of the UserController class.
hd = UserController(user_service)

router = APIRouter()


@router.get("/users", tags=["users"])
def get_users():
    return {"users": hd.get_users()}


@router.get("/users/{user}", tags=["users"])
def get_user(user: str, response: Response):
    """
    Retrieve user information based on the provided user identifier.

    Args:
        user (str): The user identifier. Can be an integer user ID, an username or an email address.
        response (Response): The FastAPI response object.

    Returns:
        The user information as a JSON response.
    """
    try:
        user = int(user)
        return hd.get_user_by_id(user, response)
    except ValueError:
        # Validate if user given is an email
        if "@" in user:
            return hd.get_user_by_email(user, response)

    return hd.get_user_by_username(user, response)


@router.post("/users", tags=["users"])
def create_user(user: UserJSON, response: Response):
    return {"user": hd.create_user(user, response)}


@router.patch("/users/{user_id}", tags=["users"])
def update_user(user_id: int, user: UserJSON):
    return {"user": hd.update_user(user_id, user)}


@router.delete("/users/{user_id}", tags=["users"])
def delete_user(user_id: int):
    return {"user": hd.delete_user(user_id)}
