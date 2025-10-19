from dataclasses import dataclass


@dataclass
class DataSourceData:
    DataSources: dict[str, str]
    Models: dict[str, str]
    MCP: dict[str, str]


class DataSources:
    def __init__(self, ds_type: str):
        self.datasource_type: str = ds_type

    def setup(self):
        pass

    def shutdown(self):
        pass


class SessionStorage:
    def __init__(self):
        pass

    async def ping(self) -> bool:
        raise NotImplementedError("Not implemented")

    async def execute(self, _query: str) -> list[tuple[str | int | float | None, ...]]:
        raise NotImplementedError("Not implemented")
