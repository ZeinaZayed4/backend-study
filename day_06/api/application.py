from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route("/")
def index():
    return "Hello!"


@app.route("/posts")
def get_posts():
    posts = Post.query.all()

    output = []
    for post in posts:
        post_data = {"name": post.name, "description": post.description}

        output.append(post_data)

    return {"posts": output}


@app.route("/posts/<id>")
def get_post(id):
    post = Post.query.get_or_404(id)
    return {"name": post.name, "description": post.description}


@app.route("/posts", methods=["POST"])
def add_post():
    post = Post(name=request.json["name"], description=request.json["description"])
    db.session.add(post)
    db.session.commit()
    return {"id": post.id}


@app.route("/posts/<id>", methods=["DELETE"])
def delete_post(id):
    post = Post.query.get(id)
    if post is None:
        return {"error": "Not found"}
    db.session.delete(post)
    db.session.commit()
    return {"message": "Post deleted"}


@app.route("/posts/<id>", methods=["PUT"])
def update_post(id):
    post = Post.query.get(id)
    if post is None:
        return {"error": "Not found"}
    post.description = request.json["description"]
    db.session.commit()
    return {"message": "Post updated"}
