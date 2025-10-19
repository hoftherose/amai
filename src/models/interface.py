from urllib.parse import ParseResult, urlparse


class Model:
    def __init__(self, endpoint: str):
        self.endpoint: ParseResult = urlparse(endpoint)
