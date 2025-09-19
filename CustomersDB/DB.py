import sqlite3

def getDbConnection() -> sqlite3.Connection:
    connection = None
    try:
        connection = sqlite3.connect("CustomersDB/Customers.db")
        connection.row_factory = sqlite3.Row
    except:
        print("Failed connecting to the DB")

    return connection

def createTablesIfNotExist():
    connection = getDbConnection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customer (
            "Id"	TEXT,
            "firstName"	TEXT,
            "lastName"	TEXT,
            "password"	TEXT,
            "username"	TEXT,
            PRIMARY KEY("Id")
        )""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Job` (
            "id"	TEXT,
            "clientId"	TEXT,
            "status"	TEXT,
            PRIMARY KEY("id")
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Order` (
            "id"	TEXT,
            "status"	TEXT,
            "customerId"	TEXT,
            "total"	NUMERIC,
            PRIMARY KEY("id")
        );
    """)
    
    connection.commit()
    connection.close()