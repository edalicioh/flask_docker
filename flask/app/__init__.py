import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
app.config.from_envvar('AppConfig')

client = MongoClient( 'mongodb://root:example@localhost:27017/todo')

db = client['list']

@app.route('/' , methods=['GET', 'POST', 'PUT' , 'DELETE'])
def hello_world():
    if request.method == 'GET':
        return "Get"
    if request.method == 'POST':
        body = request.json
        nome = body['nome']
        senha = body['senha']

        return jsonify({
            'nome': nome,
            'senha': senha
        })
        
    if request.method == 'PUT':
        return "Put"
    if request.method == 'DELETE':
        return "Delete"