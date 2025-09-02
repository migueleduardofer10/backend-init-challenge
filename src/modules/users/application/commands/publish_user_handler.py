# app/modules/users/application/handlers/publish_user_handler.py
from modules.users.application.commands import CreateUserCommand
from modules.users.infrastructure.rabbitmq_publisher import RabbitMQPublisher
from app.core.response import Response

class PublishUserHandler:
    def __init__(self, publisher: RabbitMQPublisher):
        self.publisher = publisher

    def handle(self, command: CreateUserCommand) -> Response[None]:
        self.publisher.publish_create_user(
            name=command.name,
            email=command.email,
            password=command.password,
        )
        return Response.success(None, message="User command published")
