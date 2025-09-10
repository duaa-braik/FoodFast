from DB import getDbConnection
from sqlite3 import Connection
from uuid import uuid4
from customerDb import createCustomer

def createNewUser(user) -> dict:
    connection: Connection = getDbConnection()
    try:
        userId: str = str(uuid4())
        createCustomer(user, userId, connection)
        connection.commit()
        return dict(id=userId, firstName=user['firstName'], lastName=user['lastName'])
    except:
        connection.rollback()
        raise