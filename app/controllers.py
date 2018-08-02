import jwt
from functools import wraps
from flask import jsonify, request
from app.models import Entry, User
from app.request import validate
from utils import env


class EntryController:
    def __init__(self):
        pass

    @staticmethod
    def count(auth_id):
        entry = Entry.count({'created_by': auth_id})
        return jsonify({'count': entry}), 200

    @staticmethod
    def all(auth_id):
        entries = Entry.all({'created_by': auth_id})
        return jsonify({'entries': entries, 'count': len(entries)}), 200

    @staticmethod
    def get(auth_id, entry_id):
        entry = Entry.get({'id': entry_id, 'created_by': auth_id})
        return jsonify({'entry': entry}), 200

    @staticmethod
    def create(auth_id):
        values = validate(request.json, {'title': 'required|min:5|max:255', 'body': 'required|min:10|max:1000'})
        title = values.get('title')
        body = values.get('body')
        if Entry.exists({'title': title, 'body': body, 'created_by': auth_id}):
            return jsonify({'message': 'A similar already entry exists.'}), 409
        return jsonify({'entry': Entry.create(title, body, auth_id)}), 201

    @staticmethod
    def update(auth_id, entry_id):
        values = validate(request.json, {'title': 'required|min:5|max:255', 'body': 'required|min:10|max:1000'})
        title = values.get('title')
        body = values.get('body')
        if Entry.exists({'id': entry_id, 'title': title, 'body': body, 'created_by': auth_id}):
            return jsonify({'message': 'A similar already entry exists.'}), 409
        entry = Entry.update({'id': entry_id, 'created_by': auth_id}, title, body)
        return jsonify({'entry': entry}), 200

    @staticmethod
    def delete(auth_id, entry_id):
        Entry.delete({'id': entry_id, 'created_by': auth_id})
        return jsonify({'message': 'Entry deleted.'}), 200


class UserController:
    def __init__(self):
        pass

    @staticmethod
    def signup():
        # create a new user
        values = validate(request.json, {'name': 'required', 'email': 'required|email', 'password': 'required|min:6'})
        created = User.create(values.get('name'), values.get('email'), values.get('password'))
        if created is False:
            return jsonify({'message': 'A user with the same email address exists.'}), 409
        return jsonify({'message': 'User created.'}), 201

    @staticmethod
    def login():
        data = validate(request.json, {'email': 'required|email', 'password': 'required|min:6'})
        email = data.get('email')
        password = data.get('password')
        user = User.get_by_email(email)
        if user:
            # check the user credentials
            if User.check(email, password):
                # generate jwt token
                token = User.generate_token(user)
                # return token
                return jsonify({'token': token.decode('UTF-8')}), 200
        # the user gave invalid credentials
        return jsonify({'message': 'Invalid login.'}), 401

    @staticmethod
    def check_auth(f):
        """
        This is a decorator method to wrap routes
        that require authentication.
        :param f:
        :return:
        """

        @wraps(f)
        def decorated(*args, **kwargs):
            token = None

            if 'x-access-token' in request.headers:
                token = request.headers.get('x-access-token')

            if not token:
                return jsonify({'message': 'Authentication is required.'}), 401

            try:
                data = jwt.decode(token, env('APP_KEY'))
                auth_id = data.get('id')
                print(auth_id)
            except:
                return jsonify({'message': 'Invalid access token.'}), 401

            return f(auth_id, *args, **kwargs)

        return decorated
