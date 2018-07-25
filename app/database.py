import psycopg2
from psycopg2 import sql
import psycopg2.extras
from utils import env


class DBConnection:
    def __init__(self):
        pass

    __connection = None

    @staticmethod
    def __get_connection():
        if DBConnection.__connection is None:
            host = env('DB_HOST')
            user = env('DB_USER')
            name = env('DB_NAME')
            password = env('DB_PASSWORD')
            DBConnection.__connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                dbname=name
            )
        return DBConnection.__connection

    @staticmethod
    def get():
        return DBConnection.__get_connection()


class DBQuery:
    def __init__(self, table):
        self.table = table
        self.connection = DBConnection.get()
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    @staticmethod
    def attribute_equals_value(attributes):
        """
        An sql generator for a = b, j = k, m = n ...
        :param attributes:
        """
        aggregate = []
        for item in attributes:
            aggregate.append(
                sql.SQL("{} = {}").format(
                    sql.Identifier(item), sql.Placeholder()
                )
            )
        return sql.SQL(', ').join(aggregate)

    def insert(self, data):
        """
        data is a dictionary containing field:value.
        Example {'title': 'My title', 'body': 'My body'}
        :type data: dict
        :param data:
        """
        fields = data.keys()
        values = data.values()
        query = sql.SQL("insert into {} ({}) values ({})").format(
            sql.Identifier(self.table),
            sql.SQL(', ').join(map(sql.Identifier, fields)),
            sql.SQL(', ').join(sql.Placeholder() * len(fields))
        )
        self.cursor.execute(query, values)
        self.connection.commit()

    def update(self, data, filters):
        """
        data is a dictionary containing field:value. So is
        filters. data is what will be updated and filters
        is specifies the filtering criteria.
        Examples:
        data = {'title': 'My title', 'body': 'My body'}
        filters = {'id': 7}
        :param filters: dict
        :param data: dict
        """
        sets = DBQuery.attribute_equals_value(data)
        wheres = DBQuery.attribute_equals_value(filters)
        query = sql.SQL("update {} set {} where {}").format(
            sql.Identifier(self.table),
            sets,
            wheres
        )
        values = data.values() + filters.values()
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete(self, filters):
        # delete from table where condition
        wheres = DBQuery.attribute_equals_value(filters)
        query = sql.SQL("delete from {} where {}").format(
            sql.Identifier(self.table),
            wheres
        )
        self.cursor.execute(query, filters.values())
        self.connection.commit()

    def select(self, fields, filters=None):
        if fields is '*':
            if filters is None:
                query = sql.SQL("select * from {}").format(
                    sql.Identifier(self.table)
                )
                self.cursor.execute(query)
            else:
                query = sql.SQL("select * from {} where {}").format(
                    sql.Identifier(self.table),
                    DBQuery.attribute_equals_value(filters)
                )
                self.cursor.execute(query, filters.values())
        else:
            if filters is None:
                query = sql.SQL("select {} from {}").format(
                    sql.SQL(', ').join(map(sql.Identifier, fields)),
                    sql.Identifier(self.table),
                )
                self.cursor.execute(query)
            else:
                query = sql.SQL("select {} from {} where {}").format(
                    sql.SQL(', ').join(map(sql.Identifier, fields)),
                    sql.Identifier(self.table),
                    DBQuery.attribute_equals_value(filters)
                )
                self.cursor.execute(query, filters.values())
        return self.cursor.fetchall()

    def count(self):
        query = sql.SQL("select count(*) from {}").format(sql.Identifier(self.table))
        self.cursor.execute(query)
        return self.cursor.fetchone()['count']

    def raw(self, query, fetch=False):
        self.cursor.execute(query)
        self.connection.commit()
        if fetch is True:
            return self.cursor.fetchall()
