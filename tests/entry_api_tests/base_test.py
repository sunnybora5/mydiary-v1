import unittest
from app import app
from mock import Mock
from app.models import Entry


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # Get fresh copies of mock entries
        self.entries = Mock.entries()
        Entry.set_values(Mock.entries())
        self.client = app.test_client(self)
