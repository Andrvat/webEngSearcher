from sqllite_provider import SqlLiteProvider
from data_loader import DataLoader
from usage_explorer import UsageExplorer
from argv_parser import ArgvParser
from app_view import AppView

if __name__ == "__main__":
    parser = ArgvParser()
    args = parser.get_parser().parse_args()
    provider = SqlLiteProvider(db_filename=args.dbname)

    if args.update:
        data_loader = DataLoader(provider=provider, limit=50)
        data_loader.load_titles_from('https://www.ted.com/talks/?')
        data_loader.load_subtitles_from('https://www.ted.com/talks/subtitles/id/?/lang/?')
        data_loader.load_audios_from('https://www.ted.com/talks/?')

    explorer = UsageExplorer(provider=provider)

    app = AppView(explorer=explorer)
    app.run()

    provider.close()
