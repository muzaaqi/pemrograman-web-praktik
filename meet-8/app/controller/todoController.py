from flask import request
from app import response, db
from app.controller.userController import singleTransform, transform
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

def store():
    try:
        todo = request.json.get('todo')
        desc = request.json.get('description')
        user_id = request.json.get('user_id')
        
        new_todo = Todos(user_id=user_id, todo=todo, description=desc)
        db.session.add(new_todo)
        db.session.commit()
        
        return response.ok("", "Success create new todo!")
    except Exception as e:
        print(e)
        return response.badRequest("Failed create new todo!")

def update(id):
    try:
        todo = request.json.get('todo')
        desc = request.json.get('description')
        
        todo = Todos.query.filter_by(id=id).first()
        todo.todo = todo
        todo.description = desc
        
        db.session.commit()
        
        return response.ok("", "Success update todo!")
    except Exception as e:
        print(e)
        return response.badRequest("Failed update todo!")

def show(id):
    try:
        todo = Todos.query.filter_by(id=id).first()
        if not todo:
            return response.badRequest([], "Todo not found")
        
        data = singleTransform(todo)
        return response.ok(data, "Success fetch todo")
    except Exception as e:
        print(e)
        return response.badRequest("Failed fetch todo")