from typing import Self
from dataclasses import dataclass
from urllib.parse import ParseResult, urlparse


@dataclass
class ModelConfig:
    config: dict[str, str]


class Model:
    def __init__(self, config: ModelConfig):
        self.config: ModelConfig = config
        self.endpoint: ParseResult

    def setup(self):
        pass
        # if (endpoint := self.config.get("endpoint")) is not None:
        #     self.endpoint = urlparse(endpoint)

    def shutdown(self):
        pass

    @classmethod
    def mult_parse_from_json(cls) -> list[Self]:
        return []

    @classmethod
    def parse_from_json(cls) -> Self:
        return cls(ModelConfig({}))
