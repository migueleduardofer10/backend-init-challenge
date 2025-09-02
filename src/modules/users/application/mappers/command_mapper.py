import bcrypt
from modules.users.application.commands import CreateUserCommand
from modules.users.domain.entities.user import User

# --- Mapper de comando a entidad User ---
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
