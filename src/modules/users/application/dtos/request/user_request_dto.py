from dataclasses import dataclass

@dataclass

# --- DTO para la request(petición) de creación de usuario ---
class UserRequestDTO:
    name: str
    email: str
    password: str
