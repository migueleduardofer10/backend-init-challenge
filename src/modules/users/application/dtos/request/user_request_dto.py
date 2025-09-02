from dataclasses import dataclass

@dataclass
class UserRequestDTO:
    name: str
    email: str
    password: str
