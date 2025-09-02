from modules.users.application.queries import GetUserByIdQuery, GetUserByIdHandler
from modules.users.domain.entities.user import User

class FakeUserRepository:
    def __init__(self):
        self.user = User(id=1, name="Ana", email="ana@test.com", password="hashed")

    def get_by_id(self, user_id):
        return self.user if user_id == 1 else None

def test_get_user_by_id_found():
    repo = FakeUserRepository()
    handler = GetUserByIdHandler(repo)

    query = GetUserByIdQuery(1)
    result = handler.handle(query)

    assert result is not None
    assert result.name == "Ana"

def test_get_user_by_id_not_found():
    repo = FakeUserRepository()
    handler = GetUserByIdHandler(repo)

    query = GetUserByIdQuery(99)
    result = handler.handle(query)

    assert result is None
