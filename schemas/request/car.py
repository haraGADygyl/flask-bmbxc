from marshmallow import fields

from schemas.bases import BaseCarSchema


class CarCreateRequestSchema(BaseCarSchema):
    photo = fields.String(required=True)
    photo_extension = fields.String(required=True)
