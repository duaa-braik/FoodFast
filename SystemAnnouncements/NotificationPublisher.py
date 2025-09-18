from flask import Flask, request, jsonify
from redis import Redis

app = Flask(__name__)

redisClient = Redis("localhost", port=6379)

@app.route("/publish/<channel>", methods=["POST"])
def publishAnnouncement(channel):
    announcement = request.get_json()
    redisClient.publish(channel, announcement['message'])
    return jsonify({"status": "Message sent"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)