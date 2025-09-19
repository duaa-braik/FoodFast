# Testing Guide

## 1. Account Management

This feature is built using Request-Response pattern and has 2 main API endpoints

1.  **Users Signup API** 
    ```
    curl --location 'http://127.0.0.1:3000/users' \
    --header 'Content-Type: application/json' \
    --data '{
    "firstName": "Duaa",
    "lastName": "Braik",
    "password": "123345789",
    "username": "duaa-braik55"
    }'
    ```

2. **Users Login API**
    ```
    curl --location 'http://127.0.0.1:3000/users/login' \
    --header 'Content-Type: application/json' \
    --data '{
        "username": "duaa-braik55",
        "password": "123345789"
    }'
    ```

## 2. Order Tracking

This feature is built using the Pubsub pattern using RabbitMQ as a message queue

**Steps to run this feature:**

1. Install RabbitMQ docker image
```
docker pull rabbitmq:3-management
```
2. Run RabbitMQ server (Using CMD or Docker Desktop)
```
docker run -d --name rabbitmq \
  -p 5672:5672 \
  -p 15672:15672 \
  rabbitmq:3-management
```

3. Run RabbitMQ client
```
python -m OrderTracking.OrderStatusWorker
```
4. Run Orders server
```
python -m OrderTracking.OrderService
```
5. run Restaurant server
```
python -m RestaurantNotifications.RestaurantService
```
6. Place an order
```
curl --location 'http://127.0.0.1:3005/orders' \
--header 'Content-Type: application/json' \
--data '{
    "customerId": "a34326df-4afc-4b81-8aa5-bcf5321d4f09",
    "total": 50
}'
```

## 3. Restaurant Order Notifications

**Steps to run this feature**

1. Install Redis docker image
```
docker pull redis
```
2. Run Redis server
```
docker run -d --name redis \
  -p 6379:6379 \
  redis
```
3. Run the Restaurant server
```
python -m RestaurantNotifications.RestaurantService
```
4. Open the orders dashboard in the browser
```
http://localhost:8000
``` 
5. Using the `/orders` endpoint, place an order and check the new orders at the dashboard

## 4. Customer Support Chat
**Steps to run this feature**
1. Run the first peer at port 5000 and the second one at port 5000
```
python -m CustomerSupportChat.Chat
```
2. Use Postman to send messages for both of the peers
```
-> From the left menu, click on New then choose Web Socket
-> Open 2 tabs, each for each peer
-> Peer #1 ws://localhost:5000/ws
-> Peer #2 ws://localhost:5001/ws
```
## 5. System-Wide Announcments
**Steps to run this feature**
1. Install Redis docker image
```
docker pull redis
```
2. Run Redis server
```
docker run -d --name redis \
  -p 6379:6379 \
  redis
```
3. Run the Notification Publisher
```
python -m SystemAnnouncements.NotificationPublisher 
```
4. Run the subscriber (or multiple subscribers)
```
python -m SystemAnnouncements.Subscriber
```
5. Publish a notification
```
curl --location 'http://127.0.0.1:8080/publish/new-features' \
--header 'Content-Type: application/json' \
--data '{
    "message": "Check out the new feature!"
}'
```
## 6. Image Upload for Menu Items
**Steps to run this feature**
1. Run the Image Upload server
```
python -m ImageUpload.ImageUploadService
```
2. Upload an image
```
curl --location 'http://127.0.0.1:3007/upload' \
--form 'file=@"/path/to/file"'
```
3. Check the upload status and progress
```
curl --location 'http://127.0.0.1:3007/status/<your-job-id>'
```
