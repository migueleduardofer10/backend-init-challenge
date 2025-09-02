import pytest
import bcrypt
from modules.users.application.commands import CreateUserCommand
from modules.users.application.commands import PersistUserHandler
from modules.users.domain.entities.user import User

class FakeUserRepository:
    def __init__(self):
        self.saved = None

    def save(self, user: User):
        self.saved = user
        return user

def test_persist_user_handler_saves_user():
    repo = FakeUserRepository()
    handler = PersistUserHandler(repo)

    cmd = CreateUserCommand(name="Ana", email="ana@test.com", password="secret")
    user = handler.handle(cmd)

    assert repo.saved is not None
    assert user.email == "ana@test.com"
    assert bcrypt.checkpw("secret".encode(), user.password.encode())
