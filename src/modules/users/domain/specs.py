from modules.users.domain.ports.user_repository import UserRepository
from modules.users.domain.value_objects import Email
from modules.users.domain.errors import EmailAlreadyTakenError


class EnsureEmailIsUnique:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def check(self, email: Email):
        existing = self.repo.get_by_email(email.value)
        if existing:
            raise EmailAlreadyTakenError(f"Email already taken: {email.value}")
