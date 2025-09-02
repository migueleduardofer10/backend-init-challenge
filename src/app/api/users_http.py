from fastapi import APIRouter, Depends

from modules.users.application.commands import CreateUserCommand, PublishUserHandler
from modules.users.application.queries import GetUserByIdQuery, GetUserByIdHandler
from core.providers import get_create_user_handler, get_user_by_id_handler


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def create_user(dto: CreateUserDTO):
    session = SessionLocal()
    repo = SqlAlchemyUserRepository(session)
    handler = PublishUserHandler(repo)
    command = UserRequestMapper.to_command(dto)
    resp = handler.handle(command)
    return resp.__dict__  
    
@router.get("/{user_id}")
def get_user(user_id: int):
    session = SessionLocal()
    repo = SqlAlchemyUserRepository(session)
    handler = GetUserByIdHandler(repo)
    resp = handler.handle(GetUserByIdQuery(user_id))
    return resp.__dict__