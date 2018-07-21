import json
from tests.entry_api_tests.base_test import BaseTestCase


class StatsTestCase(BaseTestCase):

    def test_it_gets_entry_count_stat(self):
        response = self.client.get('/api/v1/entries/stats/count')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual(len(self.entries), json.loads(response.data)['count'])

    def test_entry_count_remains_accurate_after_creation(self):
        data = {'title': 'A title', 'body': 'This is a body'}
        old_count = json.loads(self.client.get('/api/v1/entries/stats/count').data)['count']
        self.client.post('/api/v1/entries', data=data)
        new_count = json.loads(self.client.get('/api/v1/entries/stats/count').data)['count']
        self.assertEqual(new_count, old_count + 1)

    def test_entry_count_remains_accurate_after_deletion(self):
        old_count = json.loads(self.client.get('/api/v1/entries/stats/count').data)['count']
        self.client.delete('/api/v1/entries/4')
        new_count = json.loads(self.client.get('/api/v1/entries/stats/count').data)['count']
        self.assertEqual(new_count, old_count - 1)
