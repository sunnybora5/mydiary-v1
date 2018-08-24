from tests.profile_api_tests.base_test import BaseTestCase


class EntryTestCase(BaseTestCase):
    def test_it_gets_the_correct_entry_count(self):
        self.assertEqual(0, self.get_entry_count())
        # create entries - different user
        self.db.create_entry(count=2)
        self.assertEqual(0, self.get_entry_count())
        # create entries - current user
        self.db.create_entry(count=4, overrides={'created_by': self.user_id})
        self.assertEqual(4, self.get_entry_count())

    def test_it_gets_the_latest_entry(self):
        self.assertEqual(None, self.get_latest_entry())
        # create entries - different user
        self.db.create_entry(count=3)
        self.assertEqual(None, self.get_latest_entry())
        # create entries - current user
        last = self.db.create_entry(count=2, overrides={'created_by': self.user_id})[0]
        resp = self.get_latest_entry()
        self.assertEqual(
            {'title': last.get('title'), 'body': last.get('body')},
            {'title': resp.get('title'), 'body': resp.get('body')}
        )
