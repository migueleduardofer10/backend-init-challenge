from modules.users.domain.ports.user_repository import UserRepository
from modules.users.domain.entities.user import User


class GetUserByIdQuery:
    def __init__(self, user_id: int):
        self.user_id = user_id

class GetUserByIdHandler:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def handle(self, query: GetUserByIdQuery) -> User | None:
        return self.repo.get_by_id(query.user_id)
