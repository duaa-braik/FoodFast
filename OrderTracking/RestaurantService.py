from flask import Flask, request, jsonify
from CustomersDB.DB import getDbConnection
from sqlite3 import Connection
from .ordersDB import updateStatus, getOrderById

app = Flask(__name__)

@app.route("/changeStatus", methods=['POST'])
def changeStatus():
    connection: Connection = getDbConnection()
    try:
        orderDetails = request.get_json()
        
        if not isStatusChanged(orderDetails, connection):
            return jsonify({"message": "Order status didn't change"}), 400

        updateStatus(orderDetails, connection)
        connection.commit()
        return jsonify({"message": "success"}), 200
    except:
        connection.rollback()
        return jsonify({"message": "failed"}), 500

def isStatusChanged(orderData, connection: Connection):
    orderId = orderData['orderId']
    order = getOrderById(orderId, connection)
    oldStatus = order['status']
    return orderData['status'] != oldStatus

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3006, debug=True)