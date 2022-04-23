from sqllite_provider import SqlLiteProvider


if __name__ == "__main__":
    provider = SqlLiteProvider(db_filename='test.db')
    provider.close()
