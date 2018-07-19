from flask import make_response, jsonify
from app.models import ModelNotFoundException


class HttpHandler:
    def __init__(self):
        pass

    @staticmethod
    def handle(exception):
        if type(exception) == ModelNotFoundException:
            return HttpHandler.response(404, 'Not found.')

    @staticmethod
    def response(code, message=''):
        return make_response(jsonify({'error': message}), code)
