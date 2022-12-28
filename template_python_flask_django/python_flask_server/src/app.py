from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="../templates")


@app.route("/")
def hello_world():
    props = {}
    return render_template("index.html", props=props)


@app.route("/user/<username>", methods=["GET"])
def username(username):
    username = "admin" if username == "vincent" else "nicht admin"
    props = {"username": username}
    return render_template("index.html", props=props)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5555)
