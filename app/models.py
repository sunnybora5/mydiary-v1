from datetime import datetime
from mock import Mock
from utils import parse_date


class ModelNotFoundException(Exception):
    pass


class Entry:
    def __init__(self):
        pass

    @staticmethod
    def set_values(values):
        # Each value has an id, title, body and created_at.
        for i, entry in enumerate(values):
            values[i]['created_at'] = parse_date(entry['created_at'])
        Entry.__values = values

    # This variable is a list of entries. The entries are dictionaries.
    __values = []

    # This variable is used to ensure all values have unique ids.
    __autoincrement_id = 5  # type: int

    @staticmethod
    def get_latest_id():
        return Entry.__autoincrement_id

    @staticmethod
    def count():
        return len(Entry.__values)

    @staticmethod
    def all():
        """
        Returns all the entries.
        :rtype: list
        """
        return Entry.__values

    @staticmethod
    def get(entry_id):
        """
        Returns the specified entry.
        :param entry_id:
        :rtype: dict or None
        """
        if entry_id > Entry.__autoincrement_id:
            return None
        for entry in Entry.__values:
            if entry['id'] == entry_id:
                return entry
        return None

    @staticmethod
    def create(title, body):
        """
        Creates an entry and returns a copy.
        :rtype: dict
        """
        Entry.__autoincrement_id += 1
        entry = {
            'id': Entry.__autoincrement_id,
            'title': title,
            'body': body,
            'created_at': datetime.now()
        }
        Entry.__values.append(entry)
        return entry

    @staticmethod
    def update(entry_id, title, body):
        """
        Updates the specified entry.
        :param entry_id:
        :param title:
        :param body:
        :rtype: dict
        """
        for i, entry in enumerate(Entry.__values):
            if entry['id'] == entry_id:
                Entry.__values[i]['title'] = title
                Entry.__values[i]['body'] = body
                return Entry.__values[i]
        raise ModelNotFoundException

    @staticmethod
    def delete(entry_id):
        """
        Deletes the specified entry.
        :param entry_id:
        :rtype: bool
        """
        for i, entry in enumerate(Entry.__values):
            if entry['id'] == entry_id:
                del Entry.__values[i]
                return True
        raise ModelNotFoundException


# Initialize model with mock entries
Entry.set_values(Mock.entries())
