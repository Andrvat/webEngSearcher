from converter import convertMillis


class UsageExplorer:
    def __init__(self, provider):
        self.provider = provider

    def get_usage(self, text):
        data = self.provider.get_query_result(
            f"""
            SELECT *
            FROM contents
            JOIN titles ON contents.video_id = titles.video_id
            WHERE content LIKE '% {text} %'
            """)
        res = []
        for i, record in enumerate(data):
            res.append(record | convertMillis(record['start_time']) | {'episode_no': i + 1})
        return res
