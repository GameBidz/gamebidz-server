from fastapi import APIRouter, Response, status
from app.controllers.user_controller import UserController
from app.services.user_service import UserDefault
from app.repositories.user_repository import UserMySQL
from app.db.db import connection

rp = UserMySQL(connection)
sv = UserDefault(connection)
hd = UserController(connection)

router = APIRouter()


@router.get("/users")
def get_users():
    return {"users": hd.get_users()}


@router.get("/users/{user_id}")
def get_user_by_id(user_id: int, response: Response):
    user = hd.get_user_by_id(user_id)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "User not found"}
    return {"user": hd.get_user_by_id(user_id)}


@router.get("/users/{username}")
def get_user_by_username(username: str, response: Response):
    user = hd.get_user_by_username(username)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "User not found"}
    return {"user": hd.get_user_by_username(username)}


@router.get("/users/{email}")
def get_user_by_email(email: str, response: Response):
    user = hd.get_user_by_email(email)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "User not found"}
    return {"user": hd.get_user_by_email(email)}


@router.post("/users")
def create_user(username: str, email: str, password: str):
    return {"user": hd.create_user(username, email, password)}


@router.put("/users")
def update_user(user):
    return {"user": hd.update_user(user)}


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"user": hd.delete_user(user_id)}
