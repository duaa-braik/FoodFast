# Setup instructions

## 1. Clone the repository
```
git clone https://github.com/duaa-braik/FoodFast.git
```
## 2. install the following packages
```
pip install flask sqlite3 uuid flask_sock pika flask_sse redis 
```
## 3. Install and run RabbitMQ and Redis docker images
```
docker pull rabbitmq:3-management

docker run -d --name rabbitmq \
  -p 5672:5672 \
  -p 15672:15672 \
  rabbitmq:3-management

```
```
docker pull redis

docker run -d --name redis \
  -p 6379:6379 \
  redis

```