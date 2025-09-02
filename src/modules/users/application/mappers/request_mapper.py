from modules.users.application.dtos import UserRequestDTO
from modules.users.application.commands import CreateUserCommand

class UserRequestMapper:
    @staticmethod
    def to_command(dto: UserRequestDTO) -> CreateUserCommand:
        return CreateUserCommand(
            name=dto.name,
            email=dto.email,
            password=dto.password
        )
