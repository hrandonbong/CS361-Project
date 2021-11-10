from flask import Flask, render_template, request
import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)
cart = {}
currID = 1

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

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
        # image = request.args.get("items") + ".jpg"
        url1 = 'https://zacharylevatoncs361.herokuapp.com/images'
        myobj = {'keyword':output}
        image = requests.post(url1,data=myobj).text
        print(image)
        link = "https://www.ralphs.com/search?query=" + output
        #link = 'https://www.target.com/s?searchTerm=' + output
        #link = 'https://www.amazon.com/s?k=' + output + '&ref=nb_sb_noss_2'
        #link = 'https://www.traderjoes.com/home/search?q=' + output + '&section=products&global=yes'
        #link = 'https://www.google.com/search?q=' + output + '&authuser=2&sxsrf=AOaemvL20_aZZwfZTxM7Hr4jAgtXM7CaJA:1636496154234&source=lnms&tbm=shop&sa=X&ved=2ahUKEwibxsufp4z0AhUpJTQIHW05BRgQ_AUoAnoECAEQBA&biw=1696&bih=1336&dpr=1.5'

        price = requests.post(url2,data=myobj).text
        # price = 5


    cart[currID] = [output, image, link, price]
    currID += 1
    return render_template("index.html",items=cart)

def apiLinks(item):
        # input = request.json
        # item = input["item"]
        url = "https://www.google.com/search?q=" + item + "&tbm=shop"
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        price = soup.find("span", {"class": "HRLxBb"})
        return price.text

@app.route("/complete/<id>")
def delete(id):
    del cart[int(id)]
    if len(cart) == 0:
        return render_template("index.html")
    else:
        return render_template("index.html",items=cart)


if __name__== '__main__':
    app.run()