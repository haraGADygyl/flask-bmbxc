from marshmallow import Schema, fields, validate


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))


class UserRegisterRequestSchema(BaseUserSchema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    username = fields.String(required=True, validate=validate.Length(min=2, max=20))


class UserLoginRequestSchema(BaseUserSchema):
    pass


class AdministratorRegisterRequestSchema(UserRegisterRequestSchema):
    pass


class AdministratorLoginRequestSchema(BaseUserSchema):
    pass
