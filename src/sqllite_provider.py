import os
import sqlite3
from pathlib import Path


class SqlLiteProvider:
    def __init__(self, db_filename):
        self.connection = sqlite3.connect(db_filename)
        self.cursor = self.connection.cursor()
        self.verify_schema()

    def verify_schema(self):
        existing_tables = self.get_existing_table_names()
        dir_name = str(Path('db').resolve())
        for table_name in os.listdir(dir_name):
            if not existing_tables or table_name.split('.')[0] not in existing_tables:
                with open(os.path.join(dir_name, table_name), 'r') as query:
                    self.cursor.execute(query.read())
        self.connection.commit()

    def get_existing_table_names(self):
        self.cursor.execute(
            """
            SELECT name FROM sqlite_master
            WHERE type = 'table';
        """)
        return [list(x)[0] for x in self.cursor.fetchall()]

    def close(self):
        self.connection.close()
