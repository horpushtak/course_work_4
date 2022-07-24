from flask_restx import Namespace, Resource
from flask import request
from project.container import user_service

from project.setup.api.models import user

api = Namespace('user')


@api.route('/')
class RegisterUser(Resource):
    def get(self):
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer', '')

        return user_service.get_user_by_token(refresh_token=header)

    def patch(self):
        data = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer', '')

        return user_service.update_user(data=data, refresh_token=header)


@api.route('/password/')
class RegisterUser(Resource):
    def put(self):
        data = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer', '')

        return user_service.update_password(data=data, refresh_token=header)
