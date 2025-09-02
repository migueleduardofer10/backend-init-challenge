from dataclasses import dataclass
from modules.users.domain.errors import PasswordPolicyError


@dataclass(frozen=True)
class PasswordPolicy:
    min_length: int = 8
    require_upper: bool = True
    require_lower: bool = True
    require_digit: bool = True
    require_symbol: bool = False

    def validate(self, raw_password: str) -> None:
        p = raw_password or ""
        if len(p) < self.min_length:
            raise PasswordPolicyError(f"Password must be at least {self.min_length} characters.")
        if self.require_upper and not any(c.isupper() for c in p):
            raise PasswordPolicyError("Password must contain an uppercase letter.")
        if self.require_lower and not any(c.islower() for c in p):
            raise PasswordPolicyError("Password must contain a lowercase letter.")
        if self.require_digit and not any(c.isdigit() for c in p):
            raise PasswordPolicyError("Password must contain a digit.")
        if self.require_symbol and not any(not c.isalnum() for c in p):
            raise PasswordPolicyError("Password must contain a symbol.")
