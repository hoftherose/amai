import json
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastmcp import FastMCP
from pydantic_settings import BaseSettings

from src.models.base import Model
from src.routes import health_router, secret_router
from src.db import AmaiDataSource
from src.utils import logger

# from models.ollama_chat import response
# from src.db.sqlite import SQLiteSessionStorage


class Settings(BaseSettings):
    config_path: str = os.getenv("CONFIG_PATH", "./config/amai.json")

    def get_config(self) -> dict[str, list[AmaiDataSource] | list[Model]]:
        with open(self.config_path, "r") as f:
            # mcps: MCPConfig = MCPConfig(**json.load(f))
            data = json.load(f)
            return {
                "datasources": AmaiDataSource.mult_parse_from_json(**data),
                "models": Model.mult_parse_from_json(**data),
                # "mcp": [DataSources(ai) for ai in data.MCP],
            }


settings = Settings()

config = settings.get_config()

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
    # for sources in config["datasources"]:
    #     sources.setup()
    # Setup MCP Plugins
    logger.info("Setting up MCP Plugins")
    # Setup AI Models
    logger.info("Setting up AI Models")
    for model in config["models"]:
        model.setup()
    yield
    # Teardown Database
    logger.info("Tearing down datasources")
    # for sources in config["datasources"]:
    #     sources.shutdown()
    logger.info("Tearing down MCP Plugins")
    # Teardown MCP Plugins
    logger.info("Tearing down AI Models")
    for model in config["models"]:
        model.shutdown()
    # Teardown AI Models


app = FastAPI(lifespan=lifespan)
app.include_router(secret_router)
app.include_router(health_router)

mcp = FastMCP.from_fastapi(app)
