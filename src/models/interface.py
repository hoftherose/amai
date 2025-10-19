from dataclasses import dataclass
from urllib.parse import ParseResult, urlparse

@dataclass
class ModelConfig:
    config: dict[str, str]

class Model:
    def __init__(self, config: dict[str, str]):
        self.config: dict[str, str] = config
        self.endpoint: ParseResult

    def setup(self):
        if (endpoint := self.config.get("endpoint")) is not None:
            self.endpoint = urlparse(endpoint)

    def shutdown(self):
        pass
