from typing import override
from libsql import Cursor, connect, Connection

from src.db.base import AmaiDataSource, AmaiDataSourceConfig


class SQLiteSessionStorage(AmaiDataSource):
    def __init__(self, config: AmaiDataSourceConfig):
        super().__init__(config)
        self.url: str = self.config.connection_details.get("DB_URL", "")
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
