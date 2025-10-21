from typing import Self, override
from dataclasses import dataclass

from src.utils.interfaces import AmaiBase


@dataclass
class AmaiDataSourceConfig:
    connection_details: dict[str, str]


class AmaiDataSource(AmaiBase[AmaiDataSourceConfig]):
    def __init__(self, config: AmaiDataSourceConfig):
        super().__init__(config)

    @override
    @classmethod
    def mult_parse_from_json(cls) -> list[Self]:
        return []

    @override
    @classmethod
    def parse_from_json(cls) -> Self:
        return cls(AmaiDataSourceConfig({}))

    async def ping(self) -> bool:
        raise NotImplementedError("Not implemented")

    async def execute(self, _query: str) -> list[tuple[str | int | float | None, ...]]:
        raise NotImplementedError("Not implemented")
