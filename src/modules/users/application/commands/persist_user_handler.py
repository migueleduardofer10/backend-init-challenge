from core.base.response import Response
from modules.users.application.commands import CreateUserCommand
from modules.users.application.mappers.command_mapper import UserCommandMapper
from modules.users.infrastructure.mappers.response_mapper import UserResponseMapper
from modules.users.application.dtos import UserResponseDTO
from modules.users.domain.ports.user_repository import UserRepository
from modules.users.domain.policies import PasswordPolicy 
from modules.users.domain.value_objects import Email
from modules.users.domain.specs import EnsureEmailIsUnique
import bcrypt

class PersistUserHandler:
    def __init__(self, repo: UserRepository, password_policy: PasswordPolicy):
        self.repo = repo
        self.password_policy = password_policy

    def handle(self, command: CreateUserCommand) -> Response[UserResponseDTO]:
        email_vo = Email(command.email)
        EnsureEmailIsUnique(self.repo).check(email_vo)
        self.password_policy.validate(command.password) 
        hashed = bcrypt.hashpw(command.password.encode(), bcrypt.gensalt()).decode()
        entity = UserCommandMapper.to_entity(command)
        saved = self.repo.save(entity)
        dto = UserResponseMapper.from_entity(saved)
        return Response.success(dto, message="User created")
