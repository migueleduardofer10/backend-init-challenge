from modules.users.domain.entities.user import User
from modules.users.application.dtos import UserResponseDTO

# --- Mapper de entidad User a DTO de respuesta ---
class UserResponseMapper:
    @staticmethod
    def from_entity(user: User) -> UserResponseDTO:
        return UserResponseDTO(
            id=user.id or 0,
            name=user.name,
            email=user.email
        )
