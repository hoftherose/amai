from dataclasses import dataclass


@dataclass
class DataSourceConfig:
    datasources: dict[str, dict[str, str]]

class DataSources:
    def __init__(self, config: DataSourceConfig):
        self.config: DataSourceConfig = config

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
