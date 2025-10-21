from typing import TypeVar, Generic

from fastapi import FastAPI

AmaiType = TypeVar("AmaiType", covariant=True)
AmaiConfig = TypeVar("AmaiConfig")


class AmaiBase(Generic[AmaiConfig]):
    def __init__(self, config: AmaiConfig):
        self.config: AmaiConfig = config

    def setup(self, app: FastAPI): # pyright: ignore [reportUnusedParameter]
        pass

    def shutdown(self, app: FastAPI): # pyright: ignore [reportUnusedParameter]
        pass

    @classmethod
    def mult_parse_from_json(cls: type[AmaiType]) -> list[AmaiType]:
        raise NotImplementedError("mult_parse_from_json not implemented")

    @classmethod
    def parse_from_json(cls: type[AmaiType]) -> AmaiType:
        raise NotImplementedError("parse_from_json not implemented")
