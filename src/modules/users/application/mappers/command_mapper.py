import bcrypt
from modules.users.application.commands import CreateUserCommand
from modules.users.domain.entities.user import User

class UserCommandMapper:
    @staticmethod
    def to_entity(command: CreateUserCommand) -> User:
        hashed = bcrypt.hashpw(command.password.encode(), bcrypt.gensalt()).decode()
        return User(
            id=None,
            name=command.name,
            email=command.email,
            hashed_password=hashed
        )
