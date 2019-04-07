from flask import Flask
from flask import render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("chat.html")

@socketio.on("event")
def event_handler(json):
    if "data" in json:
        if json["data"] == "Connect":
            socketio.emit("response", {"nickname":"", "message": "새로운 유저 입장"})
    else:
        json["nickname"] = json["nickname"].encode("latin1").decode("utf-8")
        json["message"] = json["message"].encode("latin1").decode("utf-8")
        socketio.emit("response", {"nickname":json["nickname"], "message": json["message"]})
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=6700, debug=True)