from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        "title": "Post 1",
        "content": "This is the content of Post 1.",
        "author": "Stacy"
    },
    {
        "title": "Post 2",
        "content": "This is the content of Post 2."
    }
]


@app.route("/")
def hello():
    return render_template("index.html")


# use methods as list to limit access. methods if provides acts as a whitelist

@app.route("/secret", methods=["GET"])
def secret():
    return '''
        <h1>This is the /secret route</h2>
        <h2>h2</h2>
        <h3><a href="/">anchor in h3 to root</a></h3>
    '''


# this is not a query
# this is a route param like /cat

@app.route("/<string:variable>/<int:int_variable>")
def variable_example(variable, int_variable):
    return "This is the variable " + variable + ". This is the int variable " + str(int_variable)


@app.route("/posts")
def posts():
    return render_template("posts.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

