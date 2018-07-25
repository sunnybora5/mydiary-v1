import psycopg2
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
