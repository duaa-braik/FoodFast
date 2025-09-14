from flask import Flask, request, jsonify
from CustomersDB.DB import getDbConnection
from sqlite3 import Connection
from uuid import uuid4
from .ordersDB import addNewOrder

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
        return jsonify({"id": orderId, "status": status, "customerId": orderData['customerId']}), 200
    except:
        connection.rollback()
        return jsonify({"message": "internal server error"}), 500
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3005, debug=True)