from mcp.server.fastmcp import FastMCP

# Create an FastMCP server

mcp= FastMCP("Weather Service")

# Tool implementation
@mcp.tool()
def get_weather(location: str)-> str:
    """ Get currect weather for spesfic location"""
    return f"weather in {location}: Sunny, 72 F"


def get_recource(location :str)-> str:
    """Provide weather data as a resource"""
    return f"Weather data for {location}: Sunny, 72 F"
