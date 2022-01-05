import os
import uuid

from werkzeug.exceptions import NotFound

from constants import TEMP_FILE_FOLDER
from db import db
from models.car import CarModel
from services.s3 import S3Service
from util.helpers import decode_photo

s3 = S3Service()


def query_car_by_pk(pk):
    car_q = CarModel.query.filter_by(pk=pk)
    car = car_q.first()
    if not car:
        raise NotFound("This car does not exist")
    return car_q


class CarManager:
    @staticmethod
    def get_all():
        return CarModel.query.all()

    @staticmethod
    def get(pk):
        car = query_car_by_pk(pk)
        return car.first()

    @staticmethod
    def create(car_data, user_pk):
        photo_name = f"{str(uuid.uuid4())}.{car_data.pop('photo_extension')}"
        path = os.path.join(TEMP_FILE_FOLDER, photo_name)
        decode_photo(car_data.pop("photo"), path)
        photo_url = s3.upload_photo(path, photo_name)
        os.remove(path)

        car_data["photo_url"] = photo_url

        car_data["user_pk"] = user_pk.pk
        car = CarModel(**car_data)
        db.session.add(car)
        db.session.commit()
        return car

    @staticmethod
    def update(car_data, pk):
        car = query_car_by_pk(pk)
        car.update(car_data)
        db.session.add(car.first())
        db.session.commit()
        return car.first()

    @staticmethod
    def delete(pk):
        car = query_car_by_pk(pk)
        db.session.delete(car.first())
        db.session.commit()
