import os
import sqlite3
from pathlib import Path


def dict_factory(cursor, row):
    dictionary = {}
    for idx, col in enumerate(cursor.description):
        dictionary[col[0]] = row[idx]
    return dictionary


class SqlLiteProvider:
    def __init__(self, db_filename):
        self.connection = sqlite3.connect(db_filename)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        self.verify_schema()

    def verify_schema(self):
        dir_name = str(Path('db').resolve())
        for table_name in os.listdir(dir_name):
            with open(os.path.join(dir_name, table_name), 'r') as query:
                self.cursor.execute(query.read())
        self.connection.commit()

    def insert_data(self, table_name, data):
        self.cursor.executemany(
            f"""
            INSERT OR IGNORE INTO {table_name}
            VALUES (?, ?, ?, ?, ?)
            """, data)
        self.connection.commit()

    def get_query_result(self, query):
        return self.connection.execute(query).fetchall()

    def close(self):
        self.connection.close()
