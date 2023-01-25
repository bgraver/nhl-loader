import psycopg2
import psycopg2.sql as sql
from psycopg2.extras import execute_values
import os
import contextlib
from read_env import read_env

class DB:
    def __init__(self):
        self.config = read_env()
        self.conn = psycopg2.connect(
            database=self.config['POSTGRES']['PG_DATABASE'],
            user=self.config['POSTGRES']['PG_USER'],
            password=self.config['POSTGRES']['PG_PASSWORD'],
            host=self.config['POSTGRES']['PG_HOST'],
            port=self.config['POSTGRES']['PG_PORT']
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def fetch(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # TODO: checking if the return is valid
    def insert(self, dictionary, table_name):
        headers = dictionary[0].keys()
        insert_statement = "INSERT INTO {0}".format(table_name) + " ({}) VALUES %s".format(','.join(headers))
        values = [[value for value in column.values()] for column in dictionary]
        execute_values(self.cursor, insert_statement, values)
        return

    def close(self):
        self.cursor.close()
        self.conn.close()


