from modules.users.domain.entities.user import User
from modules.users.infrastructure.schemas.user_model import UserModel

# --- Mapper entre UserModel (DB) y User (entidad) ---
class UserMapper:
    @staticmethod
    def to_entity(model: UserModel) -> User:
        return User(
            id=model.id,
            name=model.vc_name,
            email=Email(model.vc_email),          # Convertir a Value Object
            hashed_password=model.vc_password,
        )

    @staticmethod
    def to_model(entity: User) -> UserModel:
        m = UserModel(
            vc_name=entity.name,
            vc_email=entity.email.value,          # Extraer string del Value Object
            vc_password=entity.hashed_password,
        )
        if entity.id is not None:
            m.id = entity.id
        return m
