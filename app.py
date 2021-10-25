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
    global currID
    if request.method == "POST":
        output = request.form.get("items")
    else:
        output = request.args.get("items")
        image = request.args.get("items") + ".jpg"
        link = "https://www.ralphs.com/search?query=" + output
    cart[currID] = [output, image, link]
    currID += 1
    return render_template("index.html",items=cart)

@app.route("/complete/<id>")
def delete(id):
    del cart[int(id)]
    return render_template("index.html",items=cart)
if __name__== '__main__':
    app.run()