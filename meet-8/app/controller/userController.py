from flask import request
from app.model.users import Users
from app import response, app
from app import db


def transform(users):
    data = []
    for user in users:
        data.append({
            'id': user.id,
            'name': user.name,
            'email': user.email
        })
    return data

def singleTransform(user):
    data = {
        'id': user.id,
        'name': user.name,
        'email': user.email
    }
    return data


def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "Success fetch all users")
    except Exception as e:
        print(e)
        return response.badRequest("Failed fetch all users")

def show(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], "User not found")
        
        data = singleTransform(user)
        return response.ok(data, "Success fetch user")
    except Exception as e:
        print(e)
        return response.badRequest("Failed fetch user")

def store():
    try:
        name = request.form.json('name')
        email = request.form.json('email')
        password = request.form.json('password')
        
        users = Users(name=name, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()
        
        data = singleTransform(users)
        return response.ok(data, "Success create new user")
        
    except Exception as e:
        print(e)
        return response.badRequest("Failed create new user")

def update(id):
    try:
        name = request.form.json('name')
        email = request.form.json('email')
        password = request.form.json('password')
        
        user = Users.query.filter_by(id=id).first()
        user.email = email
        user.name = name
        user.setPassword(password)
        
        db.session.commit()
        
        return response.ok([],"Success update user")
    except Exception as e:
        print(e)
        return response.badRequest("Failed update user")

