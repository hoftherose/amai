from typing import Self, override
from dataclasses import dataclass
from urllib.parse import ParseResult, urlparse
from src.utils.interfaces import AmaiBase


@dataclass
class ModelConfig:
    config: dict[str, str]
    model: str = "llama3.2"
    host: str = "127.0.0.1:11434"
    system: str = ""


class Model(AmaiBase[ModelConfig]):
    def __init__(self, config: ModelConfig):
        super().__init__(config)
        self.host: ParseResult

    @override
    def setup(self):
        pass
        # if (endpoint := self.config.get("endpoint")) is not None:
        #     self.endpoint = urlparse(endpoint)

    @override
    def shutdown(self):
        pass

    @override
    @classmethod
    def mult_parse_from_json(cls) -> list[Self]:
        return []

    @override
    @classmethod
    def parse_from_json(cls) -> Self:
        return cls(ModelConfig({}))
