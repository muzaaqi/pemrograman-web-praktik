from flask import request
from app import response, db
from app.controller import userController
from app.model.todos import Todos

def singleTransform(todo):
    data = {
        'id': todo.id,
        'user_id': todo.user_id,
        'todo': todo.todo,
        'description': todo.description,
        'created_at': todo.created_at,
        'updated_at': todo.updated_at,
    }
    return data

def transform(todos):
    data = []
    for todo in todos:
        data.append(singleTransform(todo))
    return data


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
        
        return response.ok(singleTransform(new_todo), "Success create new todo!")
    except Exception as e:
        print(e)
        return response.badRequest("Failed create new todo!")

def update(id):
    try:
        todo = request.json.get('todo')
        desc = request.json.get('description')
        
        todo_object = Todos.query.filter_by(id=id).first()
        todo_object.todo = todo
        todo_object.description = desc
        
        db.session.commit()
        
        return response.ok(singleTransform(todo_object), "Success update todo!")
    except Exception as e:
        print(e)
        return response.badRequest("Failed update todo!")

def show(id):
    try:
        todo = Todos.query.filter_by(id=id).first()
        if not todo:
            return response.badRequest("Todo not found")
        
        data = singleTransform(todo)
        return response.ok(data, "Success fetch todo")
    except Exception as e:
        print(e)
        return response.badRequest("Failed fetch todo")

def delete(id):
    try:
        todo = Todos.query.filter_by(id=id).first()
        if not todo:
            return response.badRequest("Todo not found")
        
        db.session.delete(todo)
        db.session.commit()
        
        return response.ok([], "Success delete todo")
    except Exception as e:
        print(e)
        return response.badRequest("Failed delete todo")

def show_by_user(user_id):
    try:
        todos = Todos.query.filter_by(user_id=user_id).all()
        data = transform(todos)
        return response.ok(data, "Success fetch todos by user")
    except Exception as e:
        print(e)
        return response.badRequest("Failed fetch todos by user")