from flask import Flask, render_template, url_for
import requests
app= Flask(__name__)


@app.route("/")
def index():
    links = {
        "Hola": "hello",
        "mostrar edad": "age",
        "mostrar posts": "posts"
    }
    return render_template("index.html", links=links)

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/age")
def age():
    age=1
    return render_template("age.html", age=age)

@app.route("/posts/all")
def posts():
    posts=requests.get("https://jsonplaceholder.typicode.com/posts").json()
    return render_template("posts.html", posts=posts)

@app.route("/posts/<id>")
def post(id):
    post=requests.get("https://jsonplaceholder.typicode.com/posts/"+id).json()
    return render_template("postid.html", post=post, id=id)