import redis

def onMessageReceive(message):
    print(f"Received message on channel '{message['channel'].decode()}': {message['data'].decode()}")

def subscribe():
    redisClient = redis.Redis(host='localhost', port=6379)
    pubsub = redisClient.pubsub()
    pubsub.subscribe('new-features', 'offers')

    print("Listening for notifications")

    for notification in pubsub.listen():
        if notification['type'] == 'message':
            onMessageReceive(notification)

if __name__ == '__main__':
    subscribe()