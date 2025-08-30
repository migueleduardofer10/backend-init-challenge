import json
import os 
import pika
import bcrypt
from sqlalchemy.orm import Session
from .database import SessionLocal, Base, engine
from ..infrastructure.db_repository import SqlAlchemyUserRepository
from ..application.commands import CreateUserCommand, CreateUserHandler


RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
QUEUE_NAME = os.getenv("RABBITMQ_QUEUE", "user.create")

def process_create_user(payload: dict): 
    name = payload["name"]
    email = payload["email"]
    password = payload["password"]

    command = CreateUserCommand(name=name, email=email, password=password)

    db: Session = SessionLocal()
    try: 
        repo = SqlAlchemyUserRepository(db)
        handler = CreateUserHandler(repo)
        handler.handle(command)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

def main():
    Base.metadata.create_all(bind=engine)

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
            ch.basic_nack(delivery_tag = method.delivery_tag)
        except Exception as e: 
            print(f"Error processing user {payload.get('email')}: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
        
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
    print(" Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    main()
