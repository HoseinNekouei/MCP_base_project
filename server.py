from mcp.server.fastmcp import FastMCP

# Create an FastMCP server

mcp= FastMCP("Weather Service")

# Tool implementation
@mcp.tool()
def get_weather(location: str)-> str:
    """ Get currect weather for spesfic location"""
    return f"weather in {location}: Sunny, 72 F"

# Resource Implementation
@mcp.resource("weather://{location}")
def get_recource(location: str)-> str:
    """Provide weather data as a resource"""
    return f"Weather data for {location}: Sunny, 72 F"

@mcp.prompt()
def weather_report(location: str) -> str:
    """ Create a weather report prompt"""
    return f"""You are a weather reporter. Weather report for {location}"""


# Run the server
if __name__== "main":
    mcp.run(transport="sse", port=3001)

