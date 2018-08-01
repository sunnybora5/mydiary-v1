from flask import Flask, redirect
from flask_cors import CORS
from app.handlers import ExceptionHandler, HttpHandler
from app.models import ModelNotFoundException
from app.controllers import EntryController, UserController
from app.request import ValidationException

# Create flask app
app = Flask(__name__)
CORS(app)


# Define API endpoints
@app.route('/')
def documentation():
    return redirect('https://mydiaryv1.docs.apiary.io')


# Entry resource routes
@app.route('/api/v1/entries/', strict_slashes=False)
@UserController.check_auth
def all_entries(auth_id):
    return EntryController.all(auth_id)


@app.route('/api/v1/entries/<int:entry_id>/', strict_slashes=False)
@UserController.check_auth
def get(auth_id, entry_id):
    return EntryController.get(auth_id, entry_id)


@app.route('/api/v1/entries/', methods=['POST'], strict_slashes=False)
@UserController.check_auth
def create(auth_id):
    return EntryController.create(auth_id)


@app.route('/api/v1/entries/<int:entry_id>/', methods=['PUT'], strict_slashes=False)
@UserController.check_auth
def update(auth_id, entry_id):
    return EntryController.update(auth_id, entry_id)


@app.route('/api/v1/entries/<int:entry_id>/', methods=['DELETE'], strict_slashes=False)
@UserController.check_auth
def delete(auth_id, entry_id):
    return EntryController.delete(auth_id, entry_id)


# Entry stats routes
@app.route('/api/v1/entries/stats/count/', methods=['GET'], strict_slashes=False)
@UserController.check_auth
def entry_stat_count(auth_id):
    return EntryController.count(auth_id)


# User routes
@app.route('/api/v1/signup/', methods=['POST'], strict_slashes=False)
def signup():
    return UserController.signup()


@app.route('/api/v1/login/', methods=['POST'], strict_slashes=False)
def login():
    return UserController.login()


# Define API error handlers
@app.errorhandler(ModelNotFoundException)
def model_not_found(exception):
    return ExceptionHandler.handle(exception)


@app.errorhandler(ValidationException)
def validation_errors(exception):
    return ExceptionHandler.handle(exception)


@app.errorhandler(404)
def not_found(error):
    return HttpHandler.handle(404)


@app.errorhandler(405)
def not_found(error):
    return HttpHandler.handle(405)


@app.errorhandler(500)
def not_found(error):
    return HttpHandler.handle(500)

