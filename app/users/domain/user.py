from dataclasses import dataclass

@dataclass
class User:
    id: int | None
    name: str
    email: str
    password: str
