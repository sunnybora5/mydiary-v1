import unittest
from mock import Mock
from app.models import Entry, ModelNotFoundException


class EntryMockModelTestCase(unittest.TestCase):
    def setUp(self):
        self.entries = Mock.entries(parse_dates=True)
        Entry.set_values(Mock.entries(parse_dates=True))

    def test_it_lists_all_entries(self):
        self.assertEqual(self.entries, Entry.all())

    def test_it_gets_a_specific_entry(self):
        # The second index of dummy entries has id == 3
        self.assertEqual(self.entries[2], Entry.get(3))
        self.assertNotEqual(self.entries[3], Entry.get(3))
        # Fails for non-existent entries
        with self.assertRaises(ModelNotFoundException):
            Entry.get(51115)

    def test_it_creates_new_entries(self):
        title = 'A title'
        body = 'A body'
        new_entry = Entry.create(title, body)
        self.assertEqual(new_entry, Entry.get(Entry.get_latest_id()))
        self.assertDictContainsSubset({'title': title, 'body': body}, new_entry)

    def test_it_increments_id(self):
        count_before = Entry.get_latest_id()
        Entry.create('Another title', 'Another body')
        self.assertEqual(count_before + 1, Entry.get_latest_id())

    def test_it_updates_entries(self):
        title = 'A new title'
        body = 'A new body'
        updated_entry = Entry.update(2, title, body)
        self.assertEqual(updated_entry, Entry.get(2))
        self.assertDictContainsSubset({'title': title, 'body': body}, updated_entry)
        # Fails for non-existent entries
        with self.assertRaises(ModelNotFoundException):
            Entry.update(71115, 'Foo', 'Bar')

    def test_it_deletes_entries(self):
        self.assertTrue(Entry.delete(3))
        # Fails for non-existent entries
        with self.assertRaises(ModelNotFoundException):
            Entry.delete(91155)

    def test_it_gets_entry_count(self):
        self.assertEqual(len(self.entries), Entry.count())

    def test_entry_count_is_always_accurate(self):
        # when new entry is created
        count_before = Entry.count()
        Entry.create('A title', 'A body')
        count_after = Entry.count()
        self.assertEqual(count_after, count_before + 1)
        # when an entry is deleted
        count_before = Entry.count()
        Entry.delete(2)
        count_after = Entry.count()
        self.assertEqual(count_after, count_before - 1)
