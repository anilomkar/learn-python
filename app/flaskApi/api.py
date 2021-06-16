import flask
import socket

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the world of Python!</h1><p>Running from server - " + socket.gethostname() + "</p>"

app.run(host='0.0.0.0')