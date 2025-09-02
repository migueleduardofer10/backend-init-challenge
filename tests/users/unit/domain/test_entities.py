import pytest
from datetime import datetime
from modules.users.domain.entities.user import User, UserStatus
from modules.users.domain.value_objects import Email
from modules.users.domain.errors import InvalidStateTransitionError

def make_user():
    return User(id=1, name="Ana", email=Email("ana@test.com"), hashed_password="x"*60)

def test_user_creation_valid():
    user = make_user()
    assert user.status == UserStatus.ACTIVE
    assert isinstance(user.created_at, datetime)

def test_rename_user():
    user = make_user()
    user.rename(" Carla ")
    assert user.name == "Carla"

def test_rename_invalid_name():
    user = make_user()
    with pytest.raises(ValueError):
        user.rename("a")

def test_suspend_and_activate():
    user = make_user()
    user.suspend()
    assert user.status == UserStatus.SUSPENDED
    user.activate()
    assert user.status == UserStatus.ACTIVE

def test_invalid_transition():
    user = make_user()
    with pytest.raises(InvalidStateTransitionError):
        user.activate()
