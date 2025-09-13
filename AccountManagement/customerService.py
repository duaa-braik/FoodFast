from DB import getDbConnection
from sqlite3 import Connection
from uuid import uuid4
from customerDb import createCustomer, getCustomerByUsername
from loginResult import LoginResult

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

def loginUser(userCreds) -> dict:
    connection: Connection = getDbConnection()
    try:
        customer = getCustomerByUsername(userCreds['username'], connection)

        if customer is None or customer['password'] != userCreds['password']:
            return dict(message="Username or password is incorrect", status= LoginResult.Fail)
        
        return dict(token="JWT token", status=LoginResult.Success)
    except:
        connection.rollback()
        raise
