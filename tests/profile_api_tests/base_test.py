import json
import unittest
from app import app
from app.models import User
from tests.helpers import DBUtils


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.db = DBUtils()
        self.db.create_schema()
        self.client = app.test_client(self)
        self.user = self.db.create_user()
        self.user_id = self.user.get('id')
        self.client = app.test_client(self)
        self.token = User.generate_token(self.user).get('token')

    def tearDown(self):
        self.db.drop_schema()

    def get_profile(self):
        return self.client.get('api/v1/profile', headers={'x-access-token': self.token})

    def __get_item(self, item):
        return json.loads(self.get_profile().data).get(item)

    def get_name(self):
        return self.__get_item('name')

    def get_since(self):
        return self.__get_item('since')

    def get_latest_entry(self):
        return self.__get_item('latest_entry')

    def get_entry_count(self):
        return self.__get_item('entry_count')

    def test_it_gets_profile_data(self):
        response = self.get_profile()
        self.assertEquals(response.status_code, 200)

    def test_it_allows_trailing_slash(self):
        self.client.get('api/v1/profile/', headers={'x-access-token': self.token})
