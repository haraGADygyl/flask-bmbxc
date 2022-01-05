import json

from flask_testing import TestCase

from config import create_my_app
from db import db
from models import UserModel


class TestAuthentication(TestCase):
    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def create_app(self):
        return create_my_app("config.TestConfig")

    def test_register_user(self):
        url = "/register"

        data = {
            "email": "test@test.com",
            "password": "123456",
            "first_name": "Test",
            "last_name": "Testov",
            "username": "test1",
        }

        users = UserModel.query.all()
        assert len(users) == 0

        resp = self.client.post(
            url, data=json.dumps(data), headers={"Content-Type": "application/json"}
        )

        assert resp.status_code == 201
        assert "token" in resp.json

        users = UserModel.query.all()
        assert len(users) == 1
