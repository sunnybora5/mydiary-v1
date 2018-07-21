import json
from tests.entry_api_tests.base_test import BaseTestCase


class ListTestCase(BaseTestCase):

    def test_it_lists_all_entries(self):
        response = self.client.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        entries = {'entries': self.entries, 'count': len(self.entries)}
        self.assertEqual(entries, json.loads(response.data))
