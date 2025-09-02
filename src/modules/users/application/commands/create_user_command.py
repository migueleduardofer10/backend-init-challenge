from dataclasses import dataclass

# --- Comando para crear un usuario ---
@dataclass
class CreateUserCommand:
    name: str
    email: str
    password: str
