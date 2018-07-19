import json
from utils import full_path


class Mock:
    def __init__(self):
        pass

    @staticmethod
    def entries():
        return Mock.__read_data('entries')

    @staticmethod
    def __read_data(resource):
        return json.load(open(full_path(resource + '.json')))
