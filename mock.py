import json
from datetime import datetime
from utils import full_path


class Mock:
    def __init__(self):
        pass

    @staticmethod
    def entries():
        entries = Mock.__read_data('entries')
        for i, entry in enumerate(entries):
            entries[i]['created_at'] = Mock.__parse_date(entries[i]['created_at'])
        return entries

    @staticmethod
    def __read_data(resource):
        return json.load(open(full_path(resource + '.json')))

    @staticmethod
    def __parse_date(date_string):
        return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
