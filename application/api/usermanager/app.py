import json
import os

from .models import *

from flask import Blueprint, Flask, request, jsonify
from flask_restplus import Api, fields, Resource
from pony.orm.serialization import to_dict

DIR = os.path.dirname(os.path.realpath(__file__))

db = Database()
db.bind(provider='mysql', host='192.168.50.7', user='usermanager_db_user', passwd='password_1', db='usermanager')

blueprint = Blueprint('api', __name__)
api = Api(app=blueprint,
          description='Web Services to manage users',
          version='1.0.0',
          doc='/docs',
          catch_all_404s=True)
ns_user_manager = api.namespace('usermanager', description='Web Service to Manage Users')


@ns_user_manager.route('/user/<id>')
class Server(Resource):

    @db_session
    def get(self, id):

        """
        GET method for the /user/<int:id> app route. This function looks up a user in the users list given the id
        in the context path of the URL
        :param id: The id in the context path of the URL, type integer
        :return: JSON response will be return either containing the data of the user to be looked up
        or an error stating that the user cannot be found
        """
        user = Person.get(id=id)
        if user is None:
            return {
                    'error' : 'user not found'
                    }, 400
        else:
            return jsonify(to_dict(user))

    @db_session
    def post(self, id):

        """
        POST method for the /user/<int:id> app route. This function creates a new user given the request data
        and the id in the context path of the URL
        :param id: The id in the context path of the URL, type integer
        :return: JSON response will be returned given the correct data had been parsed
        """
        data = request.get_json()
        try:
            user = Person(name=data['name'], lastname=data['lastname'], id=id)
            return {
                    'success' : 'user added id:{0}, {1} {2} '.format(user.id, user.name, user.lastname)
                    }, 200
        except KeyError:
            return {
                    'error' : 'user cannot be created'
                    }, 400

    @db_session
    def put(self, id):

        """
        PUT method for the /user/<int:id> app route. This function updates a user given the request data and
        the respective id
        :param id: The id in the context path of the URL, type integer
        :return: JSON response will be returned given the correct data had been parsed
        """
        data = request.get_json()

        try:
            user = Person.get(id=id)
            try:
                user.name = data['name']
                user.lastname = data['lastname']

                return {
                        'success' : 'user updated id:{0}, {1} {2} '.format(user.id, user.name, user.lastname)
                        }, 200
            except KeyError:
                return {
                        'error' : 'missing parameters in data'
                        }, 400
        except KeyError:
            return {
                    'error' : 'user cannot be found'
                    }, 400
