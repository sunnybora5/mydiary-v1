import unittest
from utils import full_path
from app.database import DBQuery, DBConnection


class QueryTestCase(unittest.TestCase):
    # before each test
    def setUp(self):
        self.table = 'entries'
        self.query = DBQuery(self.table)
        self.connection = DBConnection.get()
        self.cursor = self.connection.cursor()
        self.cursor.execute(open(full_path('schema/drop.sql'), 'r').read())
        self.cursor.execute(open(full_path('schema/create.sql'), 'r').read())
        self.connection.commit()

    # helpers
    def random(self):
        items = self.query.raw("select id from entries order by random()", True)
        return items[0] if len(items) is not 0 else None

    def create(self, count=1):
        for i in range(0, count):
            self.query.insert({'title': 'Some title', 'body': 'Some body'})

    # tests
    def test_it_inserts_records(self):
        data = {'title': 'My title', 'body': 'My body'}
        self.query.insert(data)
        self.assertTrue(data in self.query.select(['title', 'body']))

    def test_it_updates_records(self):
        self.create(10)
        record = self.random()
        data = {'title': 'Updated title', 'body': 'Updated body'}
        self.query.update(data, {'id': record['id']})
        self.assertTrue(data in self.query.select(['title', 'body']))

    def test_it_deletes_records(self):
        self.create(10)
        record = self.random()
        self.query.delete({'id': record['id']})
        self.assertEqual([], self.query.select('*', {'id': record['id']}))

    def test_it_gets_count_of_records(self):
        self.assertEqual(0, self.query.count())
        self.create(5)
        self.assertEqual(5, self.query.count())
