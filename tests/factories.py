import factory

from db import db
from models import RoleType, UserModel, CarModel


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.flush()
        return object


class UserFactory(BaseFactory):
    class Meta:
        model = UserModel

    pk = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("username")
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = RoleType.user


class CarFactory(BaseFactory):
    class Meta:
        model = CarModel

    pk = factory.Sequence(lambda n: n)
    make = factory.Faker("make")
    model = factory.Faker("model")
    color = factory.Faker("color")
    interior_color = factory.Faker("interior_color")
    tampo = factory.Faker("tampo")
    photo_url = factory.Faker("photo_url")
