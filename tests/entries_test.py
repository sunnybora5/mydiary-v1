from app import app
import unittest


class EntriesTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
