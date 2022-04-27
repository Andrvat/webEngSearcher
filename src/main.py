from sqllite_provider import SqlLiteProvider
from data_loader import DataLoader
from usage_explorer import UsageExplorer
from argv_parser import ArgvParser
import os

os.environ["KIVY_AUDIO"] = "ffpyplayer"
os.environ['KIVY_NO_ARGS'] = "1"

if __name__ == "__main__":
    parser = ArgvParser()
    args = parser.get_parser().parse_args()
    provider = SqlLiteProvider(db_filename=args.dbname)

    if args.update:
        data_loader = DataLoader(provider, limit=int(args.limit))
        data_loader.load_titles_from('https://www.ted.com/talks/?')
        data_loader.load_subtitles_from('https://www.ted.com/talks/subtitles/id/?/lang/?')
        data_loader.load_audios_from('https://www.ted.com/talks/?')

    explorer = UsageExplorer(provider)

    match args.interface:
        case 'web':
            from web_view import WebView

            app = WebView(explorer)
            app.run()
        case 'desktop':
            from desktop_view import DesktopApp

            DesktopApp(explorer).run()

    provider.close()
