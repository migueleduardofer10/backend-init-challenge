from sqlalchemy.orm import Session
from modules.users.domain.entities.user import User
from modules.users.domain.ports.user_repository import UserRepository
from modules.users.infrastructure.schemas.user_model import UserModel
from modules.users.infrastructure.mappers.user_mapper import UserMapper

# --- Implementación SQLAlchemy del UserRepository ---
class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session


    # --- Guardar usuario ---
    def save(self, user: User) -> User:
        model = UserMapper.to_model(user)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return UserMapper.to_entity(model)

    # --- Buscar usuario por ID ---
    def get_by_id(self, user_id: int) -> User | None:
        model = self.session.get(UserModel, user_id)
        return UserMapper.to_entity(model) if model else None

    # --- Buscar usuario por Email ---
    def get_by_email(self, email: str) -> User | None:
        model = self.session.query(UserModel).filter(UserModel.vc_email == email).first()
        return UserMapper.to_entity(model) if model else None
