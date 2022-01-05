from flask import request
from flask_restful import Resource

from managers.auth import AuthManager
from managers.user import UserManager, AdministratorManager
from schemas.request.user import (
    UserRegisterRequestSchema,
    UserLoginRequestSchema,
    AdministratorLoginRequestSchema,
    AdministratorRegisterRequestSchema,
)
from util.decorators import validate_schema


class Register(Resource):
    @validate_schema(UserRegisterRequestSchema)
    def post(self):
        user = UserManager.register(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 201


class Login(Resource):
    @validate_schema(UserLoginRequestSchema)
    def post(self):
        user = UserManager.login(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200


class RegisterAdministrator(Resource):
    @validate_schema(AdministratorRegisterRequestSchema)
    def post(self):
        administrator = AdministratorManager.register_administrator(request.get_json())
        token = AuthManager.encode_token(administrator)
        return {"token": token}, 201


class LoginAdministrator(Resource):
    @validate_schema(AdministratorLoginRequestSchema)
    def post(self):
        administrator = AdministratorManager.login_administrator(request.get_json())
        token = AuthManager.encode_token(administrator)
        return {"token": token}, 200
