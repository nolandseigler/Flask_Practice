from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# Needed to run flask app
app = Flask(__name__)
# Needed to run db. we can use many def databases with this not just sqlite.
# /// is relative path //// is absolute path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(app)

# dont forget to create db. GO TO TERMINAL. OPEN PYTHON TERMINAL
# TYPE  from app import db
# TYPE  db.create_all()

# You can manually add things to db by
# TYPE  from app import BlogPost
# TYPE  BlogPost.query.all() for essentially a SELECT * FROM db_table
# A list is returned so you can access with BlogPost.query.all()[0].author


# You can write data to db in term as well
# TYPE  db.session.add(BlogPost(title="Blog Post 1", content="Content of blog Post 1.", author="Bobby Saget"))

# it makes me cringe to not sep this model out

#Models
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False, default="Not Available")
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "Blog post " + str(self.id)

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


@app.route("/posts", methods=["GET", "POSTS"])
def posts():
    return render_template("posts.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

