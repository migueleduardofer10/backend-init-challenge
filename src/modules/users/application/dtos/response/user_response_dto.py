from dataclasses import dataclass

@dataclass
class UserResponseDTO:
    id: int
    name: str
    email: str