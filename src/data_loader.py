import json
import sys
import time
from urllib.error import HTTPError
from urllib.request import urlopen
from tqdm import tqdm

TOO_MANY_REQUESTS = 429


def get_parsed_subtitles(json_data, video_id):
    subtitles = json.loads(json_data)
    data = []
    for sub in subtitles['captions']:
        data.append([
            video_id,
            sub['duration'],
            sub['content'],
            sub['startOfParagraph'],
            sub['startTime']
        ])
    return data


def get_parsed_title(url_title):
    title = url_title.split('/')[-1]
    return title.replace('_', ' ')


class DataLoader:
    def __init__(self, provider, lang='en', limit=100):
        self.provider = provider
        self.where = {'contents': 'contents',
                      'titles': 'titles'}
        self.lang = lang
        self.limit = limit

    def load_subtitles_from(self, base_url):
        print('Subtitles loading...', file=sys.stderr)
        for video_id in tqdm(range(1, self.limit)):
            try:
                url = base_url.replace('?', str(video_id), 1)
                url = url.replace('?', self.lang, 1)
                with urlopen(url) as page:
                    data = get_parsed_subtitles(
                        json_data=page.read().decode('utf-8'), video_id=video_id)
                    self.provider.insert_subtitles(table_name=self.where['contents'], data=data)
            except HTTPError as e:
                if e.code == TOO_MANY_REQUESTS:
                    time.sleep(5)
                continue

    def load_titles_from(self, base_url):
        print('Video titles loading...', file=sys.stderr)
        for video_id in tqdm(range(1, self.limit)):
            url = base_url.replace('?', str(video_id), 1)
            with urlopen(url) as page:
                self.provider.insert_titles(table_name=self.where['titles'],
                                            data=[video_id, get_parsed_title(page.url)])
