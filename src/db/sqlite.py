import os
from typing import override
from libsql import Cursor, connect, Connection

from src.db.base import SessionStorage


class SQLiteSessionStorage(SessionStorage):
    def __init__(self):
        super().__init__()
        self.url: str = os.getenv("DB_URL", "")
        self.conn: Connection = connect(self.url)

    @override
    async def ping(self) -> bool:
        result: Cursor = self.conn.execute("SELECT 1")
        return result.rowcount > 0

    @override
    async def execute(self, query: str) -> list[tuple[str | int | float | None, ...]]:
        cur: Cursor = self.conn.execute(query)
        result = cur.fetchall()
        if result is None:
            return []
        return result
