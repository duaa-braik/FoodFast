from flask_sse import sse
from flask import Flask, render_template, request

app = Flask(__name__)

app.config["REDIS_URL"] = "redis://localhost:6379"
app.register_blueprint(sse, url_prefix="/stream")

@app.route("/")
def index():
    return render_template("RestaurantClient.html")

@app.route("/new-order", methods=["POST"])
def receiveNewOrder():
    order = request.get_json()
    sse.publish(order)
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
