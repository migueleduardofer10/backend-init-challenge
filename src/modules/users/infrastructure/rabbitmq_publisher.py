import json
import pika

class RabbitMQPublisher:
    def __init__(self, url: str, queue: str):
        self.url = url
        self.queue = queue

    def publish_create_user(self, name: str, email: str, password: str) -> None:
        params = pika.URLParameters(self.url)
        connection = pika.BlockingConnection(params)
        try:
            channel = connection.channel()
            channel.queue_declare(queue=self.queue, durable=True)
            payload = {"name": name, "email": email, "password": password}
            channel.basic_publish(
                exchange="",
                routing_key=self.queue,
                body=json.dumps(payload).encode(),
                properties=pika.BasicProperties(delivery_mode=2),
            )
        finally:
            connection.close()
