from utils import DATE_FORMAT
from tests.profile_api_tests.base_test import BaseTestCase


class UserTestCase(BaseTestCase):
    def test_it_gets_the_correct_name(self):
        self.assertEqual(self.user.get('name'), self.get_name())

    def test_it_gets_the_correct_since(self):
        self.assertEqual(self.user.get('created_at').strftime(DATE_FORMAT), self.get_since())
