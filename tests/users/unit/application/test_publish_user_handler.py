from modules.users.application.commands import PublishUserHandler
from modules.users.application.commands import CreateUserCommand
from modules.users.domain.policies import PasswordPolicy
from core.base.response import Response

class FakePublisher:
    def __init__(self):
        self.called = False
    def publish_create_user(self, **kwargs):
        self.called = True

def test_publish_handler_success():
    handler = PublishUserHandler(FakePublisher(), PasswordPolicy())
    cmd = CreateUserCommand(name="Ana", email="ana@test.com", password="StrongPass1")
    resp = handler.handle(cmd)
    assert resp.status_code == 200
    assert resp.message == "User command published"

def test_publish_handler_invalid_email():
    handler = PublishUserHandler(FakePublisher(), PasswordPolicy())
    cmd = CreateUserCommand(name="Ana", email="bad-email", password="StrongPass1")
    resp = handler.handle(cmd)
    assert resp.status_code == 422
