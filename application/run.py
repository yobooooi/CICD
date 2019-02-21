import os

from flask import Blueprint
from flask import Flask

DIR = os.path.dirname(os.path.realpath(__file__))

from api.bp1.app import blueprint as user_manager_api

app = Flask(__name__)

app.register_blueprint(
    user_manager_api,
    url_prefix='/api/latest')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
