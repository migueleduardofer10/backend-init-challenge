from modules.users.domain.ports.user_repository import UserRepository
from modules.users.application.dtos import UserResponseDTO
from modules.users.application.mappers.response_mapper import UserResponseMapper


class GetUserByIdHandler:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def handle(self, query: GetUserByIdQuery) -> UserResponseDTO | None:
        user = self.repo.get_by_id(query.user_id)
        return UserResponseMapper.from_entity(user) if user else None
