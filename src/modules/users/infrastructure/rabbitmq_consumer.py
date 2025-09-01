# app/modules/users/interfaces/consumer.py
import json
import pika
from core.config import settings
from core.db import SessionLocal
from modules.users.infrastructure.repositories.user_repo_sqlalchemy import SqlAlchemyUserRepository
from modules.users.application.commands import PersistUserHandler, CreateUserCommand

RABBITMQ_URL = settings.RABBITMQ_URL
QUEUE_NAME = settings.RABBITMQ_QUEUE

def build_persist_user_handler() -> PersistUserHandler:
    session = SessionLocal()
    repo = SqlAlchemyUserRepository(session)
    return PersistUserHandler(repo)
    
def process_create_user(payload: dict):
    handler = build_persist_user_handler()
    command = CreateUserCommand(
        name=payload["name"],
        email=payload["email"],
        password=payload["password"],
    )
    handler.handle(command)

def main():
    params = pika.URLParameters(RABBITMQ_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    def callback(ch, method, properties, body):
        payload = json.loads(body.decode())
        print(f"Received create user command for {payload.get('email')}")
        try:
            process_create_user(payload)
            print(f"User {payload.get('email')} created successfully")
            ch.basic_ack(delivery_tag=method.delivery_tag) 
        except Exception as e:
            print(f"Error processing user {payload.get('email')}: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)  

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    main()
