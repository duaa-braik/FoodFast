from sqlite3 import Connection

def createCustomer(customer, userId, connection: Connection):
    cursor = connection.cursor()
    cursor.execute("insert into Customer values (?, ?, ?, ?, ?)", 
                   (userId, customer['firstName'], customer['lastName'], customer['password'], customer['username']))
    
def getCustomerByUsername(username, connection: Connection):
    cusror = connection.execute("select password from Customer where username=?", (username,))
    data = cusror.fetchone()
    return dict(data) if data else None
