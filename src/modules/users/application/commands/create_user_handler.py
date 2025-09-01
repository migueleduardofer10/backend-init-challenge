# app/modules/users/application/commands.py
from dataclasses import dataclass
from modules.users.infrastructure.rabbitmq_publisher import RabbitMQPublisher

@dataclass
class CreateUserCommand:
    name: str
    email: str
    password: str

class CreateUserHandler:
    def __init__(self, publisher: RabbitMQPublisher):
        self.publisher = publisher

    def handle(self, command: CreateUserCommand) -> None:
        self.publisher.publish_create_user(
            name=command.name,
            email=command.email,
            password=command.password
        )
