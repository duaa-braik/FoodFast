from flask import Flask, request, jsonify
from CustomersDB.DB import getDbConnection
from sqlite3 import Connection
from uuid import uuid4
from .ordersDB import addNewOrder
import requests

app = Flask(__name__)

@app.route('/orders', methods=['POST'])
def createOrder():
    connection: Connection = getDbConnection()
    try:
        orderData = request.get_json()
        orderId = str(uuid4())
        status = 'Confirmed'

        addNewOrder(orderData, orderId, status, connection)
        connection.commit()

        orderData = {"id": orderId, "status": status, "customerId": orderData['customerId']}

        sendToRestaurantServer(orderData)

        return jsonify(orderData), 200
    except:
        connection.rollback()
        return jsonify({"message": "internal server error"}), 500
    
def sendToRestaurantServer(orderData):
    requests.post("http://127.0.0.1:8000/new-order", json=orderData)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3005, debug=True)