import pytest
from modules.users.domain.entities.user import User

def test_create_user_entity():
    user = User(id=1, name="Ana", email="ana@test.com", password="hashed")
    assert user.id == 1
    assert user.name == "Ana"
    assert user.email == "ana@test.com"
    assert user.password == "hashed"

def test_user_str_repr():
    user = User(id=1, name="Ana", email="ana@test.com", password="hashed")
    assert "Ana" in str(user)
