from abc import ABC, abstractmethod
from modules.users.domain.entities.user import User

# --- Puerto (Interface) de repositorio de usuarios ---
class UserRepository(ABC):

    # --- Guardar usuario ---
    @abstractmethod
    def save(self, user: User) -> User:
        pass

    # --- Obtener usuario por ID ---
    @abstractmethod
    def get_by_id(self, user_id: int) -> User | None:
        pass

    # --- Obtener usuario por email ---
    @abstractmethod
    def get_by_email(self, email: str) -> User | None: 
        pass