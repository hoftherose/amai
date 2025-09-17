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

    async def execute(self, _query: str) -> list[tuple[str | int | float, ...]]:
        raise NotImplementedError("Not implemented")

