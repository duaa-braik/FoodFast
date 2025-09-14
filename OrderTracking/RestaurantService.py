from flask import Flask, request, jsonify
from CustomersDB.DB import getDbConnection
from sqlite3 import Connection
from .ordersDB import updateStatus

app = Flask(__name__)

@app.route("/changeStatus", methods=['POST'])
def changeStatus():
    connection: Connection = getDbConnection()
    try:
        orderDetails = request.get_json()
        updateStatus(orderDetails, connection)
        connection.commit()
        return jsonify({"message": "success"}), 200
    except:
        connection.rollback()
        return jsonify({"message": "failed"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3006, debug=True)