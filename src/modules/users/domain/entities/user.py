from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from modules.users.domain.value_objects import Email
from modules.users.domain.errors import InvalidStateTransitionError




@dataclass
class User:
    id: int | None
    name: str
    email: Email
    hashed_password: str
    ## -- Campos Bitácora --- 
    status: UserStatus = UserStatus.ACTIVE
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

class UserStatus(str, Enum):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    DELETED = "DELETED"

    def __post_init__(self):
        self._validate_name()

    # --- Reglas internas ---
    def _validate_name(self):
        if not self.name or len(self.name.strip()) < 3:
            raise ValueError("Name must have at least 3 characters")
        self.name = self.name.strip()

    def rename(self, new_name: str):
        self.name = new_name.strip()
        self._validate_name()
        self._touch()

    def change_email(self, new_email: Email):
        if self.email == new_email:
            return
        self.email = new_email
        self._touch()

    def set_hashed_password(self, new_hash: str):
        if not new_hash or len(new_hash) < 20:
            raise ValueError("Invalid hashed password")
        self.hashed_password = new_hash
        self._touch()

    # --- Cambios de estado ---
    def suspend(self):
        if self.status != UserStatus.ACTIVE:
            raise InvalidStateTransitionError("Only active users can be suspended")
        self.status = UserStatus.SUSPENDED
        self._touch()

    def activate(self):
        if self.status != UserStatus.SUSPENDED:
            raise InvalidStateTransitionError("Only suspended users can be activated")
        self.status = UserStatus.ACTIVE
        self._touch()

    def delete(self):
        if self.status == UserStatus.DELETED:
            return  # idempotente
        self.status = UserStatus.DELETED
        self._touch()

    def _touch(self):
        self.updated_at = datetime.now(timezone.utc)
