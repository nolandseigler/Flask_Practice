from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"

@app.route("/secret")
def secret():
    return "This is the /secret route"


if __name__ == "__main__":
    app.run(debug=True)

