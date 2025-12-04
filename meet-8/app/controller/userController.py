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


def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "Success fetch all users")
    except Exception as e:
        print(e)
        return response.badRequest("Failed fetch all users")