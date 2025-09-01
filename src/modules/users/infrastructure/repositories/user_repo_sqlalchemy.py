from sqlalchemy.orm import Session

from modules.users.domain.entities.user import User
from modules.users.domain.ports.user_repository import UserRepository
from modules.users.infrastructure.schemas.user_model import UserModel


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, user: User) -> User:
        db_user = UserModel(name=user.name, email=user.email, password=user.password)
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return User(id=db_user.id, name=db_user.name, email=db_user.email, password=db_user.password)

    def get_by_id(self, user_id: int) -> User | None:
        db_user = self.session.get(UserModel, user_id)
        if not db_user:
            return None
        return User(id=db_user.id, name=db_user.name, email=db_user.email, password=db_user.password)
