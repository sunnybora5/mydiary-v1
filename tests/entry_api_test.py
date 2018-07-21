import json
import unittest
from app import app
from mock import Mock
from app.models import Entry
from utils import NOT_FOUND_MSG


class EntryApiTestCase(unittest.TestCase):

    def setUp(self):
        # Get fresh copies of mock entries
        self.entries = Mock.entries()
        Entry.set_values(Mock.entries())
        self.client = app.test_client(self)

    def test_it_lists_all_entries(self):
        response = self.client.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual(json.loads(response.data), {
            'entries': self.entries, 'count': len(self.entries)
        })

    def test_it_gets_a_specific_entry(self):
        response = self.client.get('/api/v1/entries/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        # The third index of mock entries has id == 4
        self.assertEqual(json.loads(response.data), {'entry': self.entries[3]})

    def test_it_creates_new_entries(self):
        new_entry = {'title': 'A title', 'body': 'A body to add'}
        response = self.client.post('/api/v1/entries', data=new_entry)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertDictContainsSubset(new_entry, json.loads(response.data)['entry'])

    def test_it_updates_entries(self):
        updates = {'title': 'A new title', 'body': 'A new body'}
        response = self.client.put('/api/v1/entries/3', data=updates)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertDictContainsSubset(updates, json.loads(response.data)['entry'])

    def test_update_fails_on_model_not_found(self):
        response = self.client.delete('/api/v1/entries/81115')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual({"error": NOT_FOUND_MSG}, json.loads(response.data))

    def test_it_deletes_entries(self):
        response = self.client.delete('/api/v1/entries/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual({'message': 'Entry deleted.'}, json.loads(response.data))
        # Ensure that entry with id == 2 no longer exists on the models
        all_entries = json.loads(self.client.get('/api/v1/entries').data)['entries']
        self.assertFalse(any(entry['id'] == 2 for entry in all_entries))

    def test_delete_fails_on_model_not_found(self):
        response = self.client.delete('/api/v1/entries/71115')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual({"error": NOT_FOUND_MSG}, json.loads(response.data))

    def test_it_gets_entry_count_stat(self):
        response = self.client.get('/api/v1/entries/stats/count')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual(len(self.entries), json.loads(response.data)['count'])

    def test_entry_count_is_always_accurate(self):
        # when new entry is created
        data = {'title': 'A title', 'body': 'This is a body'}
        old_count = json.loads(self.client.get('/api/v1/entries/stats/count').data)['count']
        self.client.post('/api/v1/entries', data=data)
        new_count = json.loads(self.client.get('/api/v1/entries/stats/count').data)['count']
        self.assertEqual(new_count, old_count + 1)
        # when an entry is deleted
        old_count = json.loads(self.client.get('/api/v1/entries/stats/count').data)['count']
        self.client.delete('/api/v1/entries/4')
        new_count = json.loads(self.client.get('/api/v1/entries/stats/count').data)['count']
        self.assertEqual(new_count, old_count - 1)

    def test_invalid_urls_trigger_not_found(self):
        responses = []
        data = {'title': 'A title', 'body': 'A body'}
        urls = ['/gibberish', '/api/v1/entries/', '/api/v1/entries/x']
        for url in urls:
            responses.append(self.client.get(url))
            responses.append(self.client.post(url, data=data))
            responses.append(self.client.put(url, data=data))
            responses.append(self.client.delete(url))
        for response in responses:
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.mimetype, 'application/json')
