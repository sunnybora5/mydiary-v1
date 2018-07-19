from flask import make_response, jsonify
from app.models import ModelNotFoundException
from utils import NOT_FOUND_MSG


class HttpHandler:
    def __init__(self):
        pass

    @staticmethod
    def handle(exception):
        if type(exception) == ModelNotFoundException:
            return HttpHandler.response(404, NOT_FOUND_MSG)

    @staticmethod
    def response(code, message=''):
        return make_response(jsonify({'error': message}), code)
