from modules.users.application.queries.get_user_by_id_handler import GetUserByIdHandler
from modules.users.application.queries import GetUserByIdQuery
from modules.users.domain.entities.user import User
from modules.users.domain.value_objects import Email
from core.base.response import Response

class FakeRepo:
    def get_by_id(self, uid):
        if uid == 1:
            return User(id=1, name="Ana", email=Email("ana@test.com"), hashed_password="x"*60)
        return None

def test_get_user_found():
    handler = GetUserByIdHandler(FakeRepo())
    resp = handler.handle(GetUserByIdQuery(1))
    assert resp.status_code == 200
    assert resp.data.name == "Ana"

def test_get_user_not_found():
    handler = GetUserByIdHandler(FakeRepo())
    resp = handler.handle(GetUserByIdQuery(99))
    assert resp.status_code == 404
