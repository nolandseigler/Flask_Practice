from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"

@app.route("/secret")
def secret():
    return "This is the /secret route"


# this is not a query
# this is a route param like /cat

@app.route("/<string:variable>/<int:int_variable>")
def variable_example(variable, int_variable):
    return "This is the variable " + variable + ". This is the int variable " + str(int_variable)


if __name__ == "__main__":
    app.run(debug=True)

