import pytest
from modules.users.domain.specs import EnsureEmailIsUnique
from modules.users.domain.entities.user import User
from modules.users.domain.errors import EmailAlreadyTakenError
from modules.users.domain.value_objects import Email

class FakeRepo:
    def __init__(self, existing=None):
        self.existing = existing
    def get_by_email(self, email):
        return self.existing if email == "taken@test.com" else None

def test_email_is_unique():
    spec = EnsureEmailIsUnique(FakeRepo())
    spec.check(Email("new@test.com"))  

def test_email_already_taken():
    spec = EnsureEmailIsUnique(
        FakeRepo(existing=User(1, "Ana", Email("taken@test.com"), "x"*60))
    )
    with pytest.raises(EmailAlreadyTakenError):
        spec.check(Email("taken@test.com"))
