from contextlib import asynccontextmanager
from typing import override

from fastapi import FastAPI
from fastmcp import FastMCP
from fastmcp.server.openapi import FastMCPOpenAPI
from pydantic_settings import BaseSettings

from src.routes import *
from src.db import DataSources
# from models.ollama_chat import response
# from src.db.sqlite import SQLiteSessionStorage

class Settings(BaseSettings):
    config_path: str = "~/.config/amai/config.json"

class Config:
    def __init__(self, settings: Settings):
        with open(settings.config_path, 'r') as f:
            self.config: str = f.read()

    @override
    def __repr__(self) -> str:
        return self.config

    def get_datasources(self) -> list[DataSources]:
        return []

settings = Settings()

@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Get Arg values
    # Get Config
    config = Config(settings)
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

