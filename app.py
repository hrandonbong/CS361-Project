from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add",methods=["GET","POST"])
def append():
    if request.method == "POST":
        output = request.form.get("items")
    else:
        output = request.args.get("items")
    return render_template("index.html",out=output)

if __name__== '__main__':
    app.run()