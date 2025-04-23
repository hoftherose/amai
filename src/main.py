# from store.app import app, mcp
# from models.ollama_chat import response
from db.sqlite import SQLiteSessionStorage
import asyncio


async def main():
    sqlite = SQLiteSessionStorage()
    if await sqlite.ping():
        print("ok")

if __name__=="__main__":
    asyncio.run(main())
