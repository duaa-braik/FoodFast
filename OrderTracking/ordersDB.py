from sqlite3 import Connection

def addNewOrder(orderData, orderId, status, connection: Connection):
    cursor = connection.cursor()
    cursor.execute("insert into `Order` values (?,?,?,?)", 
                (orderId, status, orderData['customerId'], orderData['total'],))
    
def updateStatus(order, connection: Connection):
    cursor = connection.cursor()
    cursor.execute("update `Order` set status=? where id=?", (order['status'], order['orderId']))