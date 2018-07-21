from flask import Flask
from app.handlers import ExceptionHandler, HttpHandler
from app.models import ModelNotFoundException
from app.controllers import EntryController
from app.request import ValidationException

# Create flask app
app = Flask(__name__)


# Define API endpoints
# Entry resource routes
@app.route('/api/v1/entries')
def all_entries():
    return EntryController.all()


@app.route('/api/v1/entries/<int:entry_id>')
def get(entry_id):
    return EntryController.get(entry_id)


@app.route('/api/v1/entries', methods=['POST'])
def create():
    return EntryController.create()


@app.route('/api/v1/entries/<int:entry_id>', methods=['PUT'])
def update(entry_id):
    return EntryController.update(entry_id)


@app.route('/api/v1/entries/<int:entry_id>', methods=['DELETE'])
def delete(entry_id):
    return EntryController.delete(entry_id)


# Entry stats routes
@app.route('/api/v1/entries/stats/count', methods=['GET'])
def entry_stat_count():
    return EntryController.count()


# Define API error handlers
@app.errorhandler(ModelNotFoundException)
def model_not_found(exception):
    return ExceptionHandler.handle(exception)


@app.errorhandler(ValidationException)
def model_not_found(exception):
    return ExceptionHandler.handle(exception)


@app.errorhandler(404)
def not_found(error):
    return HttpHandler.handle(404)
