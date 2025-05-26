import asyncio
import argparse

class Config:
    def __init__(self, path: str):
        return path


async def main() -> None:
    # Get Arg values
    parser = argparse.ArgumentParser('')
    _ = parser.add_argument('--config_path', help='Path to Amai configuration file', type=str)
    # Get Config
    args = parser.parse_args()
    config: str = args.config_path # pyright: ignore[reportAny]
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
    # Setup MCP Plugins
    # Setup AI Models
    pass

if __name__=='__main__':
    asyncio.run(main())
