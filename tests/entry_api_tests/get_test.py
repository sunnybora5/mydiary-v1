import json
from tests.entry_api_tests.base_test import BaseTestCase


class GetTestCase(BaseTestCase):

    def test_it_gets_a_specific_entry(self):
        response = self.client.get('/api/v1/entries/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        # The third index of mock entries has id == 4
        self.assertEqual(json.loads(response.data), {'entry': self.entries[3]})
