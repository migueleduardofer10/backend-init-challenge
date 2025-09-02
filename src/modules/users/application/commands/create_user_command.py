# app/modules/users/application/commands.py
from dataclasses import dataclass


@dataclass
class CreateUserCommand:
    name: str
    email: str
    password: str
