# Backend communication patterns: FoodFast Delivery Platform

FoodFast is a food delivery platform which connects customers, restaurants and delivery drivers, and it has multiple features where each of them is implemented using a backend commounication pattern that best suites it

## 1. Customer Account Management

#### **Pattern:** Request-Response

#### **Analysis:**

* The user needs to get immediate reponse whening creating a new account, logging in and updating their data

## 2. Order Tracking for Customers

#### **Pattern:** PubSub using RabbitMQ
#### **Analysis:**

The restaurant updates the order status as follows:
```
Confirmed -> Preparing -> Ready -> Picked up -> Delivered
```
* While the user can check for the order periodically, but its crucial to conserve users' mobile battery life
* The system has +1000 online users in peak hours
* The PubSub pattern suites this feature because it provides scalability and off loads the server

## 3. Restaurant Order Notifications

#### **Pattern:** Server-Sent Events (SSE) 
#### **Analysis:**

* The restaurant staff needs to receive new orders in real time
* the orders dashboard should automatically update
* Reststaurants receive many orders during peak hours and no orders should be missed
* Multiple staff members maybe logged in at the same time
* The SSE option is very great for real-time updates as it sends multiple events over the same connections

## 4. Customer Support Chat

#### **Pattern:** WebSocket
#### **Analysis:**

* Messages are sent between the customer and the support team in a bi-directional way
* Message should be received instantly
* the Websocket best suites this feature because it proveide a very low latency as it runs over TCP and because the connection it provides is full-duplex

## 5. System-Wide Annaouncements

#### **Pattern:** PubSub (Redis)
#### **Analysis:**

* Restaurants can send notifications to thousands of users about service outages, updates, new features and offers
* The server should not be overwhelemed when sending the notifications
* Redis pubsub best suites this feature because it has the ability to publish messages to all users at once, and because this will off load the server as the message broker takes the responsibility to brodcast messages to the users

## 6. Image Upload for Menu Items

#### **Pattern:** Short Polling
#### **Analysis:**

* Restaurants can upload images for menu items
* The upload process takes some time but it can be estimated
* The user don't need to wait (be blocked) until the upload and processing of the image completes
* Using short polling, the upload process happens in the background, and the user receives a jobID which can be used to check for the upload status and progress
* It best suites this feature because it doesn't block the users and allows for asynchronous processing