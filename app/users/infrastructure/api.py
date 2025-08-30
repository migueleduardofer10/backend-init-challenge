from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..application.commands import CreateUserCommand, CreateUserHandler
from ..application.queries import GetUserByIdQuery, GetUserByIdHandler
from .db_repository import SqlAlchemyUserRepository
from .database import get_session
from .rabbitmq_publisher import publish_create_user

router = APIRouter(prefix="/users2", tags=["users"])

@router.post("/")
def create_user(name: str, email: str, password: str):
    print(">>> Llamando al ENDPOINT NUEVO <<<")
    publish_create_user(name,email,password)
    return {"status": "queued"}

@router.get("/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_session)):
    repo = SqlAlchemyUserRepository(session)
    handler = GetUserByIdHandler(repo)
    query = GetUserByIdQuery(user_id)
    user = handler.handle(query)
    if not user:
        return {"error": "User not found"}
    return {"id": user.id, "name": user.name, "email": user.email}
