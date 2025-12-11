from flask import request
from app import response, db
from app.controller.userController import transform
from app.model.todo import Todos


def index():
    try:
        id = request.args.get('user_id')
        todos = Todos.query.filter_by(user_id=id).all()
        data = transform(todos)
        return response.ok(data, "Success fetch all todos")
    except Exception as e:
        print(e)
        return response.badRequest("Failed fetch all todos")
