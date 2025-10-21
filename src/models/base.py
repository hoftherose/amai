from typing import Self, override
from dataclasses import dataclass
from urllib.parse import ParseResult, urlparse

from fastapi import FastAPI
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
    def setup(self, app: FastAPI):
        self.host = urlparse(self.config.host)

    @override
    def shutdown(self, app: FastAPI):
        pass

    @override
    @classmethod
    def mult_parse_from_json(cls) -> list[Self]:
        return []

    @override
    @classmethod
    def parse_from_json(cls) -> Self:
        return cls(ModelConfig({}))
