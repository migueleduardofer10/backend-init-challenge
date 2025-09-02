import pytest
from modules.users.domain.policies import PasswordPolicy
from modules.users.domain.errors import PasswordPolicyError

policy = PasswordPolicy()

def test_valid_password():
    assert policy.validate("StrongPass1") is None

def test_too_short_password():
    with pytest.raises(PasswordPolicyError):
        policy.validate("123")

def test_missing_uppercase():
    with pytest.raises(PasswordPolicyError):
        policy.validate("password1")
