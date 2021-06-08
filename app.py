from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import flask_restful
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item,ItemList

app = Flask(__name__)

app.secret_key="diwu" #usualyy the secret key should be in an environment variable to ensure security of the application
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth
 

       

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True) 