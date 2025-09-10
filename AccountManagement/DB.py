import sqlite3

def getDbConnection() -> sqlite3.Connection:
    connection = None
    try:
        connection = sqlite3.connect("Customers.db")
    except:
        print("Failed connecting to the DB")

    return connection