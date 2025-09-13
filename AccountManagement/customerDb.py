from sqlite3 import Connection

def createCustomer(customer, userId, connection: Connection):
    cursor = connection.cursor()
    cursor.execute("insert into Customer values (?, ?, ?, ?, ?)", 
                   (userId, customer['firstName'], customer['lastName'], customer['password'], customer['username']))
