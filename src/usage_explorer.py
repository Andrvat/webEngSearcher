class UsageExplorer:
    def __init__(self, provider):
        self.provider = provider

    def get_usage(self, text):
        return self.provider.get_query_result(
            f"""
            SELECT * FROM contents
            WHERE content LIKE '% {text} %'
            """)
