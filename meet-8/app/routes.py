from app import app
from flask import request
from app.controller import userController
from app.controller import todoController

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

@app.route('/login', methods=['POST'])
def login():
    return userController.login()

@app.route('/todos', methods=['POST'])
def todos():
    return todoController.store()

@app.route('/todos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def todosAction(id):
    if request.method == 'GET':
        return todoController.show(id)
    elif request.method == 'PUT':
        return todoController.update(id)
    elif request.method == 'DELETE':
        return todoController.delete(id)

@app.route('/todos/user/<int:user_id>', methods=['GET'])
def todosByUser(user_id):
    return todoController.show_by_user(user_id)