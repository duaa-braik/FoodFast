from CustomersDB.DB import getDbConnection
from sqlite3 import Connection
from uuid import uuid4
from .customerDb import createCustomer, getCustomerByUsername
from .result import Result

def createNewUser(user) -> dict:
    connection: Connection = getDbConnection()
    try:
        username = user['username']
        customer = getCustomerByUsername(username, connection)
        
        if customer is not None:
            return dict(message="Username already exists", status= Result.Fail)

        userId: str = str(uuid4())
        createCustomer(user, userId, connection)
        connection.commit()
        return dict(id=userId, firstName=user['firstName'], lastName=user['lastName'])
    except:
        connection.rollback()
        raise

def loginUser(userCreds) -> dict:
    connection: Connection = getDbConnection()
    try:
        customer = getCustomerByUsername(userCreds['username'], connection)

        if customer is None or customer['password'] != userCreds['password']:
            return dict(message="Username or password is incorrect", status= Result.Fail)
        
        return dict(token="JWT token", status=Result.Success)
    except:
        connection.rollback()
        raise
