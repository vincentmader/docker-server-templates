from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, docker-python-flask!</p>"


if __name__ == "__main__":
    print("Hello, python3!")
    app.run(host='0.0.0.0', debug=True, port=5555)
