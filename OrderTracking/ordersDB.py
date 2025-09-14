from sqlite3 import Connection

def addNewOrder(orderData, orderId, status, connection: Connection):
    cursor = connection.cursor()
    cursor.execute("insert into `Order` values (?,?,?,?)", 
                (orderId, status, orderData['customerId'], orderData['total'],))
    
def updateStatus(order, connection: Connection):
    cursor = connection.cursor()
    cursor.execute("update `Order` set status=? where id=?", (order['status'], order['orderId']))

def getOrderById(orderId, connection: Connection):
    cusror = connection.execute("select status from `Order` where id=?", (orderId,))
    data = cusror.fetchone()
    return dict(data) if data else None