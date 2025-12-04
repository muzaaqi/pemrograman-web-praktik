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

@app.route('/users/<int:id>')
def usesrDetail(id):
    return userController.show(id)

@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return userController.index()
    else:
        return userController.store()