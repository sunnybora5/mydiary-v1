import unittest
from faker import Faker
from app import app
from tests.helpers import DBUtils


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        self.db = DBUtils()
        self.db.drop_schema()
        self.db.create_schema()
        self.client = app.test_client(self)
