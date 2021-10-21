from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

cart_put_args = reqparse.RequestParser()
cart_put_args.add_argument("name",type=str,help="Name of Item",required=True)

cart = {}

class shopping(Resource):
    def get(self, item_id):
        return cart[item_id]

    def put(self, item_id):
        args = cart_put_args.parse_args()
        cart[item_id] = args
        return cart[item_id], 201
api.add_resource(shopping, "/shopping/<int:item_id>")

if __name__== '__main__':
    app.run(debug=True)