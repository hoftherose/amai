import asyncio
import argparse
from .api import app # pyright: ignore[reportUnusedImport]
from .db import DataSources

class Config:
    def __init__(self, path: str):
        with open(path, 'r') as f:
            config = Config(f.read())
            return config

    def get_datasources(self) -> list[DataSources]:
        return []


async def main() -> None:
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
    pass

if __name__=='__main__':
    asyncio.run(main())
