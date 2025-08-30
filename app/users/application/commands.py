from ..domain.user import User
from ..domain.user_repository import UserRepository
import bcrypt

class CreateUserCommand:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

class CreateUserHandler:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def handle(self, command: CreateUserCommand) -> User:
        hashed_pw = bcrypt.hashpw(command.password.encode(), bcrypt.gensalt())
        user = User(id=None, name=command.name, email=command.email, password=hashed_pw.decode())
        return self.repo.save(user)
