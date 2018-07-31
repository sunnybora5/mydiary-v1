import json
import unittest
from faker import Faker
from app import app
from tests.helpers import DBUtils


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        self.db = DBUtils()
        self.db.create_schema()
        self.client = app.test_client(self)

    def post(self, url, data):
        return self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json'
        )

    def tearDown(self):
        self.db.drop_schema()
