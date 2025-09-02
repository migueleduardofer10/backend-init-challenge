# app/modules/users/application/handlers/publish_user_handler.py
from modules.users.application.commands import CreateUserCommand
from modules.users.infrastructure.rabbitmq_publisher import RabbitMQPublisher
from core.base.response import Response
from modules.users.domain.value_objects import Email
from modules.users.domain.policies import PasswordPolicy


class PublishUserHandler:
    def __init__(self, publisher: RabbitMQPublisher, password_policy: PasswordPolicy):
        self.publisher = publisher
        self.password_policy = password_policy

    def handle(self, command: CreateUserCommand) -> Response[None]:
        try:
            Email(command.email) 
            self.password_policy.validate(command.password) 
        except Exception as e:
            return Response.error(str(e), status_code=422)

        self.publisher.publish_create_user(
            name=command.name,
            email=command.email,
            password=command.password,
        )
        return Response.success(None, message="User command published")
