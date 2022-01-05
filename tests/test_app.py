import json

from flask_testing import TestCase

from config import create_my_app
from db import db


class TestApplication(TestCase):
    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def create_app(self):
        return create_my_app("config.TestConfig")

    def test_get_all(self):
        url = "/car"

        resp = self.client.get(url)

        assert resp.status_code == 200

    def test_authentication_missing_auth_header_raises(self):

        url_methods = [
            ("/car/create", "POST"),
            ("/car/edit/1", "PUT"),
            ("/car/delete/1", "DELETE"),
        ]

        for url, method in url_methods:
            if method == "POST":
                resp = self.client.post(url, data=json.dumps({}))
            elif method == "PUT":
                resp = self.client.put(url, data=json.dumps({}))
            else:
                resp = self.client.delete(url)

            assert resp.status_code == 400
            assert resp.json == {"message": "Invalid token"}
