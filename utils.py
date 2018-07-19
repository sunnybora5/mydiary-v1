import os

ROOT_DIRECTORY = os.path.dirname(__file__)


def full_path(path):
    return ROOT_DIRECTORY + '/' + path
