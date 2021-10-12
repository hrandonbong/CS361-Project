from flask import Flask, render_template, request

app = Flask(__name__)
SESSION = Reward()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/",methods=["GET"])
def ret():
    add = request.args.get("item")
    return render_template("index.html",out=add)