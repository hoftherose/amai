import os
from typing import override
from libsql_experimental import Connection, connect, Cursor

from src.db.base import SessionStorage

class SQLiteSessionStorage(SessionStorage):
    def __init__(self):
        super().__init__()
        self.url: str = os.getenv("DB_URL", "")
        self.conn: Connection = connect(self.url)

    async def cursor(self) -> Cursor:
        return self.conn.cursor()

    @override
    async def ping(self) -> bool:
        cur = await self.cursor()
        result = cur.execute("SELECT 1")
        return result.rowcount > 0

    @override
    async def execute(self, query: str) -> list[tuple[str | int | float, ...]]:
        cur = await self.cursor()
        result = cur.execute(query)
        return result.fetchall()

