from app import app
from flask import request
from app.controller import userController

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/users')
def users():
    return userController.index()

@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def userDetail(id):
    if request.method == 'GET':
        return userController.show(id)
    elif request.method == 'PUT':
        return userController.update(id)
    elif request.method == 'DELETE':
        return userController.delete(id)

@app.route('/users', methods=['POST', 'GET'])
def addUsers():
    if request.method == 'GET':
        return userController.index()
    else:
        return userController.store()
