from fastapi import APIRouter, Depends

from modules.users.application.commands import CreateUserCommand, CreateUserHandler
from modules.users.application.queries import GetUserByIdQuery, GetUserByIdHandler
from core.providers import get_create_user_handler, get_user_by_id_handler


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def create_user(
    name: str,
    email: str,
    password: str,
    handler: CreateUserHandler = Depends(get_create_user_handler),
):
    handler.handle(CreateUserCommand(name, email, password))
    return {"status": "queued"}
    
@router.get("/{user_id}")
def get_user(
    user_id: int,
    handler: GetUserByIdHandler = Depends(get_user_by_id_handler),
):
    query = GetUserByIdQuery(user_id)
    user = handler.handle(query)
    if not user:
        return {"error": "User not found"}
    return {"id": user.id, "name": user.name, "email": user.email}
