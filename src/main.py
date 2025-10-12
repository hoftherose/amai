import json
from contextlib import asynccontextmanager
from typing import TypedDict

from fastapi import FastAPI
from fastmcp import FastMCP
from fastmcp.server.openapi import FastMCPOpenAPI
from pydantic_settings import BaseSettings

from src.routes import *
from src.db import DataSources, DataSourceData
from src.utils import logger

# from models.ollama_chat import response
# from src.db.sqlite import SQLiteSessionStorage


class Settings(BaseSettings):
    config_path: str = "./config/amai.json"

    def get_config(self) -> dict[str, list[DataSources]]:
        with open(self.config_path, "r") as f:
            data: DataSourceData = DataSourceData(json.load(f))
            return {
                "datasources": [DataSources(ds) for ds in data.DataSources],
            }


settings = Settings()


class Config(TypedDict):
    datasources: list[DataSources]
    # plugins: List[Plugins]
    # models: List[Models]


config = Config(datasources=[])

"""
Config Setup
{
    DataSources: [{...}],
    Plugins: [{...}],
    Models: [{...}],
}
"""


@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Setup Database
    logger.info("Setting up datasources")
    for sources in config["datasources"]:
        sources.setup()
    # Setup MCP Plugins
    logger.info("Setting up MCP Plugins")
    # Setup AI Models
    logger.info("Setting up AI Models")
    yield
    # Teardown Database
    logger.info("Tearing down datasources")
    for sources in config["datasources"]:
        sources.shutdown()
    logger.info("Tearing down MCP Plugins")
    # Teardown MCP Plugins
    logger.info("Tearing down AI Models")
    # Teardown AI Models


app: FastAPI = FastAPI(lifespan=lifespan)
app.include_router(secret_router)
app.include_router(health_router)

mcp: FastMCPOpenAPI = FastMCP.from_fastapi(app)

# async def main():
#     sqlite = SQLiteSessionStorage()
#     if await sqlite.ping():
#         print("ok")
