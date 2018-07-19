from flask import jsonify, request
from app.models import Entry


class EntryController:
    def __init__(self):
        pass

    @staticmethod
    def all():
        entries = Entry.all()
        return jsonify({'entries': entries, 'count': len(entries)}), 200

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
        return jsonify(Entry.update(entry_id, title, body)), 200

    @staticmethod
    def delete(entry_id):
        Entry.delete(entry_id)
        return jsonify({'message': 'Entry deleted.'}), 200
