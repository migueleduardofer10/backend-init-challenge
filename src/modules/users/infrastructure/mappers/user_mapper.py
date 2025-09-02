from modules.users.domain.entities.user import User
from modules.users.infrastructure.schemas.user_model import UserModel

class UserMapper:
    @staticmethod
    def to_entity(model: UserModel) -> User:
        return User(
            id=model.i_user_id,
            name=model.vc_name,
            email=model.vc_email,
            hashed_password=model.vc_password,
        )

    @staticmethod
    def to_model(entity: User) -> UserModel:
        m = UserModel(
            vc_name=entity.name,
            vc_email=entity.email,
            vc_password=entity.hashed_password,
        )
        # i_user_id puede ser None al crear; si viene seteado, lo asignamos
        if entity.id is not None:
            m.i_user_id = entity.id
        return m
