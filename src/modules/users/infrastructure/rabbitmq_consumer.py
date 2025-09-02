import json
import pika
from dependency_injector.wiring import inject, Provide

from app.core.container import Container
from modules.users.application.commands import CreateUserCommand
from modules.users.application.handlers.persist_user_handler import PersistUserHandler


def process_create_user(payload: dict, handler: PersistUserHandler):
    command = CreateUserCommand(
        name=payload["name"],
        email=payload["email"],
        password=payload["password"],
    )
    handler.handle(command)


def main():
    # Inicializamos el container
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    params = pika.URLParameters(container.config().RABBITMQ_URL())
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=container.config().RABBITMQ_QUEUE(), durable=True)

    @inject
    def callback(
        ch,
        method,
        properties,
        body,
        handler: PersistUserHandler = Provide[Container.persist_user_handler],
    ):
        payload = json.loads(body.decode())
        print(f"Received create user command for {payload.get('email')}")
        try:
            process_create_user(payload, handler)
            print(f"User {payload.get('email')} created successfully")
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Error processing user {payload.get('email')}: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=container.config().RABBITMQ_QUEUE(),
        on_message_callback=callback,
    )

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    main()
