from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from core.container import Container
from modules.users.application.dtos import UserRequestDTO
from modules.users.application.mappers.request_mapper import UserRequestMapper
from modules.users.application.commands import PublishUserHandler
from modules.users.application.queries import GetUserByIdQuery, GetUserByIdHandler


router = APIRouter(prefix="/users", tags=["users"])

# --- Endpoint para crear un usuario ---
@router.post("/")
@inject
def create_user(
    dto: UserRequestDTO,
    handler: PublishUserHandler = Depends(Provide[Container.publish_user_handler]),
):
    command = UserRequestMapper.to_command(dto)
    resp = handler.handle(command)
    return resp.__dict__

# --- Endpoint para obtener un usuario por ID ---
@router.get("/{user_id}")
@inject
def get_user(
    user_id: int,
    handler: GetUserByIdHandler = Depends(Provide[Container.get_user_by_id_handler]),
):
    resp = handler.handle(GetUserByIdQuery(user_id))
    return resp.__dict__
