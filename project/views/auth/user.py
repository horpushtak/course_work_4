from flask_restx import Namespace, Resource
from flask import request
from project.container import user_service
from project.setup.api.models import user

api = Namespace('user')


@api.route('/register/')
class RegisterUser(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.create_user()
        return "Не достаточно данных"


# @api.route('/login')
