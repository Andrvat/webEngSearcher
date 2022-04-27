usage: main.py [-h] --dbname DBNAME --update | --no-update --limit LIMIT [--interface {web,desktop}]

Happy English Part

options:

  -h, --help            show this help message and exit

  --dbname DBNAME       SqlLite database filename

  --update, --no-update
                        Is needed to make requests for data uploading (long
                        loading is possible)

  --limit LIMIT         Limit of downloading audio tracks from TED videos

  --interface {web,desktop}
                        Type of interested interface: web or desktop app
