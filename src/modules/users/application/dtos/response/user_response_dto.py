from dataclasses import dataclass

@dataclass

# --- DTO para la response de usuario ---
class UserResponseDTO:
    id: int
    name: str
    email: str