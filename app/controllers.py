from flask import jsonify, request, abort
from app.models import Entry


class EntryController:
    def __init__(self):
        pass

    @staticmethod
    def all():
        return jsonify({'entries': Entry.all()}), 200

    @staticmethod
    def get(entry_id):
        return jsonify({'entry': Entry.get(entry_id)}), 200

    @staticmethod
    def create():
        title = request.form['title']
        body = request.form['body']
        return jsonify(Entry.create(title, body)), 201

    @staticmethod
    def update(entry_id):
        title = request.form['title']
        body = request.form['body']
        result = Entry.update(entry_id, title, body)
        if isinstance(result, dict):
            return jsonify(result), 200
        abort(result)

    @staticmethod
    def delete(entry_id):
        result = Entry.delete(entry_id)
        if result is True:
            return jsonify({'message': 'Entry deleted.'}), 200
        abort(result)
