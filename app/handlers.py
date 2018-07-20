from flask import make_response, jsonify
from app.models import ModelNotFoundException
from utils import NOT_FOUND_MSG


class Handler:

    def __init__(self):
        pass

    @staticmethod
    def response(code, message=''):
        return make_response(jsonify({'error': message}), code)


class ExceptionHandler(Handler):
    def __init__(self):
        pass

    @staticmethod
    def handle(exception):
        if type(exception) == ModelNotFoundException:
            return ExceptionHandler.response(404, NOT_FOUND_MSG)


class HttpHandler(Handler):
    def __init__(self):
        pass

    @staticmethod
    def handle(code):
        if code == 404:
            return ExceptionHandler.response(404, NOT_FOUND_MSG)
