import bcrypt
from modules.users.domain.entities.user import User
from modules.users.domain.ports.user_repository import UserRepository
from modules.users.application.commands import CreateUserCommand


class PersistUserHandler:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def handle(self, command: CreateUserCommand) -> User:
        hashed_pw = bcrypt.hashpw(command.password.encode(), bcrypt.gensalt())

        user = User(
            id=None,
            name=command.name,
            email=command.email,
            password=hashed_pw.decode(),
        )

        return self.repo.save(user)
