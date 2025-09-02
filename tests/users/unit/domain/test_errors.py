from modules.users.domain.errors import (
    EmailInvalidError,
    EmailAlreadyTakenError,
    PasswordPolicyError,
    InvalidStateTransitionError,
    UserNotFoundError,
)

def test_error_hierarchy():
    e = EmailInvalidError("bad email")
    assert isinstance(e, Exception)
    assert isinstance(e, EmailInvalidError)
    assert issubclass(EmailAlreadyTakenError, Exception)
