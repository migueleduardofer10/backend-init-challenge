# --- Errores de dominio ---
class DomainError(Exception):
    """Base para errores de dominio."""

class EmailInvalidError(DomainError):
    pass

class EmailAlreadyTakenError(DomainError):
    pass

class PasswordPolicyError(DomainError):
    pass

class InvalidStateTransitionError(DomainError):
    pass

class UserNotFoundError(DomainError):
    pass