from marshmallow import fields, validate

from schemas.bases import BaseCarSchema


class CarCreateResponseSchema(BaseCarSchema):
    pk = fields.Integer(required=True)
    photo_url = fields.String(required=True, validate=validate.Length(max=255))
    created_on = fields.DateTime(required=True)
