import os
from typing import override
from libsql_client import create_client, Client, ResultSet # pyright: ignore[reportMissingTypeStubs]

from db.base import SessionStorage

class SQLiteSessionStorage(SessionStorage):
    def __init__(self):
        super().__init__()
        self.url: str = os.getenv("DB_URL", "")

    async def client(self) -> Client:
        return create_client(self.url)

    @override
    async def ping(self) -> bool:
        client: Client = await self.client()
        result: ResultSet = await client.execute("SELECT 1")
        return len(result.rows) > 0

