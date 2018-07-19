from os.path import dirname
from datetime import datetime


MODEL_NOT_FOUND = 404
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
ROOT_DIRECTORY = dirname(__file__)


def full_path(path=None):
    if path is None:
        return ROOT_DIRECTORY
    return ROOT_DIRECTORY + '/' + path


def parse_date(date_string):
    return datetime.strptime(date_string, DATE_FORMAT)

