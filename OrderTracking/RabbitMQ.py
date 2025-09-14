import pika
import json

def getRabbitMQConnection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))
    return connection

def publishMessageToQueue(message):
    rabbitMQ = getRabbitMQConnection()
    channel = rabbitMQ.channel()
    channel.queue_declare(queue="Orders")

    channel.basic_publish(
        exchange="",
        routing_key="Orders",
        body=json.dumps(message)
    )

    rabbitMQ.close()