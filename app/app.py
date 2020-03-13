import os
import json

from flask import Flask , jsonify
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
api = Api(app)

# nessesario pra pegar os argumentos
parser = reqparse.RequestParser()
parser.add_argument('nome')

class Todo(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        return jsonify({ parser.parse_args()['nome'] })

api.add_resource(Todo, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')