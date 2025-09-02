import pytest
from modules.users.domain.value_objects import Email
from modules.users.domain.errors import EmailInvalidError

def test_valid_email():
    email = Email("valid@test.com")
    assert str(email) == "valid@test.com"

def test_invalid_email():
    with pytest.raises(EmailInvalidError):
        Email("not-an-email")
