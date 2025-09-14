from flask import Flask, request, jsonify
from customerService import createNewUser, loginUser
from result import Result

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def createUser():
    try: 
        userData = request.get_json()
        createUserResult = createNewUser(userData)

        if createUserResult.get('status') == Result.Fail:
            return jsonify({"message": createUserResult['message']}), 400
        
        return jsonify(createUserResult), 201
    except:
        return jsonify({"message": "Internal server error"}), 500

@app.route('/users/login', methods=['POST'])
def login():
    try:
        userCreds = request.get_json()
        result = loginUser(userCreds)
    
        if result['status'] == Result.Fail:
            return jsonify({"message": result['message']}), 401
        elif result['status'] == Result.Success:
            return jsonify({ "access_token": result['token'] })
    except:
        return jsonify({"message": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
