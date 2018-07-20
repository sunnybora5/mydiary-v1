import json
from utils import full_path, parse_date


class Mock:
    def __init__(self):
        pass

    @staticmethod
    def entries(parse_dates=False):
        entries = Mock.__read_data('entries')
        if parse_dates is True:
            for i, entry in enumerate(entries):
                entries[i]['created_at'] = parse_date(entry['created_at'])
                entries[i]['updated_at'] = parse_date(entry['updated_at'])
        return entries

    @staticmethod
    def __read_data(resource):
        return json.load(open(full_path(resource + '.json')))
