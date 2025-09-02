from modules.users.application.dtos import UserRequestDTO
from modules.users.application.commands import CreateUserCommand

# --- Mapper de DTO de request a comando ---
class UserRequestMapper:
    @staticmethod
    def to_command(dto: UserRequestDTO) -> CreateUserCommand:
        return CreateUserCommand(
            name=dto.name,
            email=dto.email,
            password=dto.password
        )
