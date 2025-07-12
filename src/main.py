import argparse
from typing import override
from contextlib import asynccontextmanager

from .db import DataSources

from src.routes import *
from fastapi import FastAPI
from fastmcp import FastMCP
from fastmcp.server.openapi import FastMCPOpenAPI
# from models.ollama_chat import response
# from src.db.sqlite import SQLiteSessionStorage

@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Get Arg values
    parser = argparse.ArgumentParser('')
    _ = parser.add_argument('--config_path', help='Path to Amai configuration file', type=str)
    # Get Config
    args = parser.parse_args()
    config = Config(args.config_path) # pyright: ignore[reportAny]
    print(config)
    """
    Config Setup
    {
        DataSources: [{...}],
        Plugins: [{...}],
        Models: [{...}],
    }
    """
    # Setup Database
    for sources in config.get_datasources():
        sources.setup()
    # Setup MCP Plugins
    # Setup AI Models
    yield
    # Teardown Database
    for sources in config.get_datasources():
        sources.shutdown()
    # Teardown MCP Plugins
    # Teardown AI Models

app: FastAPI = FastAPI(lifespan=lifespan)
app.include_router(secret_router)
app.include_router(health_router)

mcp: FastMCPOpenAPI = FastMCP.from_fastapi(app)

# async def main():
#     sqlite = SQLiteSessionStorage()
#     if await sqlite.ping():
#         print("ok")

class Config:
    def __init__(self, path: str):
        with open(path, 'r') as f:
            self.config: str = f.read()

    @override
    def __repr__(self) -> str:
        return self.config

    def get_datasources(self) -> list[DataSources]:
        return []


