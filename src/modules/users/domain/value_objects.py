import re
from dataclasses import dataclass
from modules.users.domain.errors import EmailInvalidError

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# --- Value Object para Email ---
@dataclass(frozen=True)
class Email:
    value: str

    # --- Validar formato del email ---
    def __post_init__(self):
        v = self.value.strip().lower()
        if not EMAIL_RE.match(v):
            raise EmailInvalidError(f"Invalid email: {self.value}")
        object.__setattr__(self, "value", v)

    def __str__(self):
        return self.value
