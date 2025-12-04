from app.model.users import Users
from app import response, app


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