from sqlalchemy import func

from db import db


class CarModel(db.Model):
    __tablename__ = "cars"

    pk = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(32), nullable=False)
    model = db.Column(db.String(32), nullable=False)
    color = db.Column(db.String(32), nullable=False)
    interior_color = db.Column(db.String(32), nullable=False)
    tampo = db.Column(db.String(32), nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    user_pk = db.Column(db.Integer, db.ForeignKey("users.pk"))
    user = db.relationship("UserModel")
