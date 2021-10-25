from flask import Flask, render_template, request

app = Flask(__name__)
cart = {}
currID = 1

@app.route("/")
def index():
    return render_template("index.html")

#--------- HTTP REQUEST ----------#
@app.route("/add",methods=["GET","POST"])
def append():
    if request.method == "POST":
        output = request.form.get("items")
    else:
        output = request.args.get("items")
        item = request.args.get("items") + ".jpg"
        link = "https://www.google.com/search?q=" + output
    cart[output] = [currID, item, link]
    return render_template("index.html",items=cart)

if __name__== '__main__':
    app.run()