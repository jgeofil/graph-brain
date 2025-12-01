from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

# Construct server URL with authentication
from urllib.parse import urlencode
import os

base_url = "https://server.smithery.ai/@LinkupPlatform/linkup-mcp-server/mcp"
params = {"api_key": os.getenv("SMITHERY_API_KEY")}
url = f"{base_url}?{urlencode(params)}"
follow_path = "linkup-search"
sub_path = f"{base_url}/{follow_path}"


async def main():
    # Connect to the server using HTTP client
    async with streamablehttp_client(url) as (read, write, _):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools(sub_path)
            print(f"Available tools: {', '.join([t.name for t in tools_result.tools])}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
