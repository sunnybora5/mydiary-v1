from datetime import datetime
from mock import Mock


class ModelNotFoundException(Exception):
    pass


class Entry:
    def __init__(self):
        pass

    @staticmethod
    def set_values(values):
        Entry.__entries = values

    # This variable is a list of entries. The entries are dictionaries.
    __entries = []

    # This variable is used to ensure all values have unique ids.
    __autoincrement_id = 5  # type: int

    @staticmethod
    def __get_entry_index(entry_id):
        for i, entry in enumerate(Entry.__entries):
            if entry['id'] == entry_id:
                return i
        raise ModelNotFoundException

    @staticmethod
    def get_latest_id():
        return Entry.__autoincrement_id

    @staticmethod
    def count():
        return len(Entry.__entries)

    @staticmethod
    def all():
        """
        Returns all the entries.
        :rtype: list
        """
        return Entry.__entries

    @staticmethod
    def get(entry_id):
        """
        Returns the specified entry.
        :param entry_id:
        :rtype: dict or None
        """
        return Entry.__entries[Entry.__get_entry_index(entry_id)]

    @staticmethod
    def create(title, body):
        """
        Creates an entry and returns a copy.
        :rtype: dict
        """
        Entry.__autoincrement_id += 1
        now = datetime.now()
        entry = {
            'id': Entry.__autoincrement_id,
            'title': title,
            'body': body,
            'created_at': now,
            'updated_at': now
        }
        Entry.__entries.append(entry)
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
        index = Entry.__get_entry_index(entry_id)
        Entry.__entries[index]['title'] = title
        Entry.__entries[index]['body'] = body
        Entry.__entries[index]['updated_at'] = datetime.now()
        return Entry.__entries[index]

    @staticmethod
    def delete(entry_id):
        """
        Deletes the specified entry.
        :param entry_id:
        :rtype: bool
        """
        del Entry.__entries[Entry.__get_entry_index(entry_id)]
        return True


# Initialize model with mock entries
Entry.set_values(Mock.entries(parse_dates=True))
