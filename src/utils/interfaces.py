from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from fastapi import FastAPI

AmaiType = TypeVar("AmaiType", covariant=True)
AmaiConfig = TypeVar("AmaiConfig")


class AmaiBase(Generic[AmaiConfig], ABC):
    def __init__(self, config: AmaiConfig):
        self.config: AmaiConfig = config

    @abstractmethod
    def setup(self, app: FastAPI):
        pass

    @abstractmethod
    def shutdown(self, app: FastAPI):
        pass

    @abstractmethod
    @classmethod
    def mult_parse_from_json(cls: type[AmaiType]) -> list[AmaiType]:
        raise NotImplementedError("mult_parse_from_json not implemented")

    @abstractmethod
    @classmethod
    def parse_from_json(cls: type[AmaiType]) -> AmaiType:
        raise NotImplementedError("parse_from_json not implemented")
