from modules.users.application.dtos import CreateUserDTO
from modules.users.application.commands import CreateUserCommand

class UserRequestMapper:
    @staticmethod
    def to_command(dto: CreateUserDTO) -> CreateUserCommand:
        return CreateUserCommand(
            name=dto.name,
            email=dto.email,
            password=dto.password
        )
