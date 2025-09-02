from modules.users.domain.ports.user_repository import UserRepository
from modules.users.application.dtos import UserResponseDTO
from modules.users.infrastructure.mappers.response_mapper import UserResponseMapper
from modules.users.application.queries import GetUserByIdQuery
from modules.users.domain.errors import UserNotFoundError
from core.base.response import Response

# --- Handler para obtener usuario por ID ---
class GetUserByIdHandler:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def handle(self, query: GetUserByIdQuery) -> Response[UserResponseDTO | None]:
        try:
            user = self.repo.get_by_id(query.user_id)                                   # Buscar usuario en repo
            if not user:
                raise UserNotFoundError(f"User with id {query.user_id} not found")

            dto = UserResponseMapper.from_entity(user)
            return Response.success(dto, message="User found")

        except UserNotFoundError as e:
            return Response.error(str(e), status_code=404)