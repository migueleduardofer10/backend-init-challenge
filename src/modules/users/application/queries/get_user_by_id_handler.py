from modules.users.domain.ports.user_repository import UserRepository
from modules.users.application.dtos import UserResponseDTO
from modules.users.infrastructure.mappers.response_mapper import UserResponseMapper
from modules.users.application.queries import GetUserByIdQuery

class GetUserByIdHandler:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def handle(self, query: GetUserByIdQuery) -> UserResponseDTO | None:
        user = self.repo.get_by_id(query.user_id)
        return UserResponseMapper.from_entity(user) if user else None
