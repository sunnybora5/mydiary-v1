import jwt
import datetime
from flask import jsonify, request
from app.models import Entry, User
from app.request import validate
from utils import env


class EntryController:
    def __init__(self):
        pass

    @staticmethod
    def count():
        return jsonify({'count': Entry.count()}), 200

    @staticmethod
    def all():
        entries = Entry.all()
        return jsonify({'entries': entries, 'count': len(entries)}), 200

    @staticmethod
    def get(entry_id):
        return jsonify({'entry': Entry.get(entry_id)}), 200

    @staticmethod
    def create():
        validate(request.form, {'title': 'required|min:5|max:255', 'body': 'required|min:10|max:1000'})
        entry = Entry.create(request.form['title'], request.form['body'])
        return jsonify({'entry': entry}), 201

    @staticmethod
    def update(entry_id):
        validate(request.form, {'title': 'required|min:5|max:255', 'body': 'required|min:10|max:1000'})
        entry = Entry.update(entry_id, request.form['title'], request.form['body'])
        return jsonify({'entry': entry}), 200

    @staticmethod
    def delete(entry_id):
        Entry.delete(entry_id)
        return jsonify({'message': 'Entry deleted.'}), 200


class UserController:
    def __init__(self):
        pass

    @staticmethod
    def signup():
        # create a new user
        validate(request.form, {'name': 'required', 'email': 'required|email', 'password': 'required|min:6'})
        created = User.create(request.form['name'], request.form['email'], request.form['password'])
        if created is False:
            return jsonify({'message': 'A user with the same email address exists.'}), 409
        return jsonify({'message': 'User created.'}), 201

    @staticmethod
    def login():
        auth = request.authorization
        # check that username(email in this case) and password are provided.
        if not auth or not auth.username or not auth.password:
            message = {'error': 'Login required.'}
        else:
            # check that the user actually exists
            user = User.get_by_email(auth.username)

            if user:
                # check the user credentials
                if User.check(auth.username, auth.password):
                    # token payload
                    payload = {
                        'user': user['email'],
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=int(env('SESSION_LIFETIME')))
                    }
                    # generate jwt token
                    token = jwt.encode(payload, env('APP_KEY'))
                    # return token
                    return jsonify({'token': token.decode('UTF-8')}), 200
            # the user gave invalid credentials
            message = {'error': 'Invalid login.'}
        return jsonify(message), 401
