from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from app.core.providers import Container
from modules.users.application.dtos import CreateUserDTO
from modules.users.application.mappers.request_mapper import UserRequestMapper
from modules.users.application.handlers.publish_user_handler import PublishUserHandler
from modules.users.application.handlers.get_user_by_id_handler import GetUserByIdHandler, GetUserByIdQuery

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
@inject
def create_user(
    dto: CreateUserDTO,
    handler: PublishUserHandler = Depends(Provide[Container.publish_user_handler]),
):
    command = UserRequestMapper.to_command(dto)
    resp = handler.handle(command)
    return resp.__dict__

@router.get("/{user_id}")
@inject
def get_user(
    user_id: int,
    handler: GetUserByIdHandler = Depends(Provide[Container.get_user_by_id_handler]),
):
    resp = handler.handle(GetUserByIdQuery(user_id))
    return resp.__dict__
