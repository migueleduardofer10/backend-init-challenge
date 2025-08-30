from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..application.commands import CreateUserCommand, CreateUserHandler
from ..application.queries import GetUserByIdQuery, GetUserByIdHandler
from .db_repository import SqlAlchemyUserRepository
from .database import get_session

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def create_user(name: str, email: str, password: str, session: Session = Depends(get_session)):
    repo = SqlAlchemyUserRepository(session)
    handler = CreateUserHandler(repo)
    command = CreateUserCommand(name, email, password)
    user = handler.handle(command)
    return {"id": user.id, "name": user.name, "email": user.email}

@router.get("/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_session)):
    repo = SqlAlchemyUserRepository(session)
    handler = GetUserByIdHandler(repo)
    query = GetUserByIdQuery(user_id)
    user = handler.handle(query)
    if not user:
        return {"error": "User not found"}
    return {"id": user.id, "name": user.name, "email": user.email}
