from sqllite_provider import SqlLiteProvider
from data_loader import DataLoader


if __name__ == "__main__":
    provider = SqlLiteProvider(db_filename='test.db')
    data_loader = DataLoader(provider=provider)
    data_loader.load_subtitles_from('https://www.ted.com/talks/subtitles/id/?/lang/?')
    provider.close()
