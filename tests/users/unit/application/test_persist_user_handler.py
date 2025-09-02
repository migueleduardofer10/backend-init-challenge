# --- Tests de PersistUserHandler ---
from modules.users.application.commands.persist_user_handler import PersistUserHandler
from modules.users.application.commands import CreateUserCommand
from modules.users.domain.policies import PasswordPolicy
from core.base.response import Response

# --- Fake repo para pruebas ---
class FakeRepo:
    def __init__(self):
        self.saved = None
    def save(self, user): 
        self.saved = user
        return user
    def get_by_email(self, email): 
        return None

# --- Test persistencia exitosa ---
def test_persist_user_handler_success():
    handler = PersistUserHandler(FakeRepo(), PasswordPolicy())
    cmd = CreateUserCommand(name="Ana", email="ana@test.com", password="StrongPass1")
    resp = handler.handle(cmd)
    assert isinstance(resp, Response)
    assert resp.status_code == 200
