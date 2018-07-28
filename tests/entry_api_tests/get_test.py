import json
from tests.entry_api_tests.base_test import BaseTestCase


class GetTestCase(BaseTestCase):

    def test_it_gets_a_specific_entry(self):
        record = self.db.create_entry()
        response = self.get('/api/v1/entries/%s' % str(record['id']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        expected_data = {'title': record['title'], 'body': record['body']}
        self.assertDictContainsSubset(expected_data, json.loads(response.data)['entry'])
