import argparse


class ArgvParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Happy English Part')
        self.parser.add_argument('--dbname',
                                 type=str,
                                 help='SqlLite database filename',
                                 required=True)
        self.parser.add_argument('--update',
                                 default=True,
                                 action=argparse.BooleanOptionalAction,
                                 help='Is needed to make requests for data uploading',
                                 required=True)

    def get_parser(self):
        return self.parser
