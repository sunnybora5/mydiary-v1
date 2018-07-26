from flask import jsonify, request
from app.models import Entry
from app.request import validate


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
        return jsonify({'message': 'Signup is not implemented.'})

    @staticmethod
    def login():
        # generate and return token if user has
        return jsonify({'message': 'Log in is not implemented.'})
