# --- Tests de PasswordPolicy ---
import pytest
from modules.users.domain.policies import PasswordPolicy
from modules.users.domain.errors import PasswordPolicyError

policy = PasswordPolicy()

# --- Test contraseña válida ---
def test_valid_password():
    assert policy.validate("StrongPass1") is None

# --- Test contraseña demasiado corta ---
def test_too_short_password():
    with pytest.raises(PasswordPolicyError):
        policy.validate("123")

# --- Test falta de mayúscula ---
def test_missing_uppercase():
    with pytest.raises(PasswordPolicyError):
        policy.validate("password1")
