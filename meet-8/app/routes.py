from app import app
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