import json
import unittest
from app import app
from mock import Mock
from app.models import Entry


class EntryApiTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.entries = Mock.entries()
        Entry.set_values(self.entries)

    def test_it_lists_all_entries(self):
        response = self.client.get('/entries')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual(json.loads(response.data), {'entries': self.entries})

    def test_it_gets_a_specific_entry(self):
        response = self.client.get('/entries/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        # The third index of mock entries has id == 4
        self.assertEqual(json.loads(response.data), {'entry': self.entries[3]})

    def test_it_creates_new_entries(self):
        new_entry = {'title': 'A title', 'body': 'A body'}
        response = self.client.post('/entries', data=new_entry)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertDictContainsSubset(new_entry, json.loads(response.data))

    def test_it_updates_entries(self):
        updates = {'title': 'A new title', 'body': 'A new body'}
        response = self.client.put('/entries/3', data=updates)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertDictContainsSubset(updates, json.loads(response.data))

    def test_it_deletes_entries(self):
        response = self.client.delete('/entries/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        all_entries = json.loads(self.client.get('/entries').data)
        # Ensure that entry with id == 3 no longer exists on the models
        self.assertFalse(any(entry['id'] == 2 for entry in all_entries))
