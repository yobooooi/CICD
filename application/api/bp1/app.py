import json
import os

from flask import Blueprint, Flask, request
from flask_restplus import Api, fields, Resource

DIR = os.path.dirname(os.path.realpath(__file__))

blueprint = Blueprint('api', __name__)
api = Api(app=blueprint,
          description='Web Services to manage users',
          version='1.0.0',
          doc='/docs',
          catch_all_404s=True)
ns_user_manager = api.namespace('usermanager', description='Web Service to Manage Users')


class User():
    def __init__(self, name, lastname, id):
        self.name = name
        self.lastname = lastname
        self.id = id

    def __repr__(self):
        return [self.id, self.name, self.lastname]

users = {}

id = 1
user = User(name='John', lastname='Doe', id=id)
users[id]=user


@ns_user_manager.route('/user/<int:id>')
class Server(Resource):

    def get(self, id):
        """
        GET method for the /user/<int:id> app route. This function looks up a user in the users list given the id
        in the context path of the URL
        :param id: The id in the context path of the URL, type integer
        :return: JSON response will be return either containing the data of the user to be looked up
        or an error stating that the user cannot be found
        """
        try:
            return {
                    'id': users[id].id,
                    'name': users[id].name,
                    'surname': users[id].lastname
                    }
        except KeyError:
            return {
                    'error' : 'user cannot be found'
                    }

    def post(self, id):
        """
        POST method for the /user/<int:id> app route. This function creates a new user given the request data
        and the id in the context path of the URL
        :param id: The id in the context path of the URL, type integer
        :return: JSON response will be returned given the correct data had been parsed
        """
        data = request.get_json()
        try:
            user = User(name=data['name'], lastname=data['lastname'], id=id)
            users[id] = user

            return {
                    'success' : 'user added id:{0}, {1} {2} '.format(user.id, user.name, user.lastname)
                    }
        except KeyError:
            return {
                    'error' : 'user cannot be created'
                    }

    def put(self, id):
        """
        PUT method for the /user/<int:id> app route. This function updates a user given the request data and
        the respective id
        :param id: The id in the context path of the URL, type integer
        :return: JSON response will be returned given the correct data had been parsed
        """
        data = request.get_json()

        try:
            users[id]
            try:
                users[id].name = data['name']
                users[id].lastname = data['lastname']

                return {
                        'success' : 'user updated id:{0}, {1} {2} '.format(user.id, user.name, user.lastname)
                        }
            except KeyError:
                return {
                        'error' : 'missing parameters in data'
                        }
        except KeyError:
            return {
                    'error' : 'user cannot be found'
                    }
