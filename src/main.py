from src.routes import *
from fastapi import FastAPI
from fastmcp import FastMCP
from fastmcp.server.openapi import FastMCPOpenAPI
# from models.ollama_chat import response
from src.db.sqlite import SQLiteSessionStorage

app: FastAPI = FastAPI()
app.include_router(secret_router)
app.include_router(health_router)

mcp: FastMCPOpenAPI = FastMCP.from_fastapi(app)

async def main():
    sqlite = SQLiteSessionStorage()
    if await sqlite.ping():
        print("ok")

