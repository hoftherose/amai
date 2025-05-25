class SessionStorage:
    def __init__(self):
        pass

    async def ping(self) -> bool:
        raise NotImplementedError("Not implemented")

    async def execute(self, _query: str) -> list[tuple[str, ...]]:
        raise NotImplementedError("Not implemented")

