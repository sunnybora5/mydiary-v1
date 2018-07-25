import psycopg2
from utils import env


class DBConnection:
    def __init__(self):
        pass

    __host = env('DB_HOST')
    __user = env('DB_USER')
    __name = env('DB_NAME')
    __password = env('DB_PASSWORD')

    __connection = None

    @staticmethod
    def get():
        if DBConnection.__connection is None:
            DBConnection.__connection = psycopg2.connect(
                host=DBConnection.__host,
                user=DBConnection.__user,
                password=DBConnection.__password,
                dbname=DBConnection.__name
            )
        return DBConnection.__connection
