from flask import Flask, request, jsonify
from customerService import createNewUser

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def createUser():
    try: 
        userData = request.get_json()
        createdUser = createNewUser(userData)
        return jsonify(createdUser), 201
    except:
        return jsonify({"message": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
