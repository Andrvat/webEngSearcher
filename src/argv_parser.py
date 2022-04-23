import argparse


class ArgvParser:
    def __init__(self):
        # https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
        self.parser = argparse.ArgumentParser(description='Happy English Part')
        self.parser.add_argument('--dbname',
                                 type=str,
                                 help='SqlLite database filename')
        self.parser.add_argument('--update',
                                 default=True,
                                 action=argparse.BooleanOptionalAction,
                                 help='Is needed to make requests for data uploading')

    def get_parser(self):
        return self.parser
