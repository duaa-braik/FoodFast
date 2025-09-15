import pika, json

def onMessageReceive(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f"Your order is: {message['status']}")

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", port=5672)
    )
    channel = connection.channel()

    channel.queue_declare(queue="Orders")

    channel.basic_consume(
        queue="Orders",
        on_message_callback=onMessageReceive,
        auto_ack=True
    )

    print("Waiting for messages. Press CTRL+C to exit")
    channel.start_consuming()

if __name__ == "__main__":
    main()
