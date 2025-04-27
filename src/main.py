from src.store.app import app, mcp # pyright: ignore reportUnusedImport
# from models.ollama_chat import response
from src.db.sqlite import SQLiteSessionStorage


async def main():
    sqlite = SQLiteSessionStorage()
    if await sqlite.ping():
        print("ok")

