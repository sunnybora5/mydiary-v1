from app.database import DBQuery


class ModelNotFoundException(Exception):
    pass


class Entry:
    __db = DBQuery('entries')

    def __init__(self):
        pass

    @staticmethod
    def __check(entry_id):
        if Entry.__db.exists(entry_id) is False:
            raise ModelNotFoundException

    @staticmethod
    def count():
        return Entry.__db.count()

    @staticmethod
    def all():
        """
        Returns all the entries.
        :rtype: list
        """
        return Entry.__db.select('*')

    @staticmethod
    def get(entry_id):
        """
        Returns the specified entry.
        :param entry_id:
        :rtype: dict or None
        """
        Entry.__check(entry_id)
        return Entry.__db.get(entry_id)

    @staticmethod
    def create(title, body):
        """
        Creates an entry and returns a copy.
        :rtype: dict
        """
        return Entry.__db.insert({
            'title': title,
            'body': body,
        })

    @staticmethod
    def update(entry_id, title, body):
        """
        Updates the specified entry.
        :param entry_id:
        :param title:
        :param body:
        :rtype: dict
        """
        Entry.__check(entry_id)
        return Entry.__db.update({'title': title, 'body': body}, {'id': entry_id})

    @staticmethod
    def delete(entry_id):
        """
        Deletes the specified entry.
        :param entry_id:
        :rtype: bool
        """
        Entry.__check(entry_id)
        return Entry.__db.delete({'id': entry_id})
