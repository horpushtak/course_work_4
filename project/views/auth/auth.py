from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user

api = Namespace('auth')


@api.route('/register/')
class RegisterView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.create_user(data.get('email'), data.get('password')), 201
        return "Не достаточно данных", 503


@api.route('/login/')
class LoginView(Resource):
    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.check_user(data.get('email'), data.get('password')), 201
        return "Не достаточно данных", 503

    def put(self):
        data = request.json
        if data.get('asses_token') and data.get('refresh_token'):
            return user_service.update_token(data.get('refresh_token'))
        return "Не достаточно данных", 503