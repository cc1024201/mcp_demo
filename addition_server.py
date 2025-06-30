#!/usr/bin/env python3
"""
Simple MCP Server - Addition Tool
This is a basic example of an MCP (Model Context Protocol) server
that provides a tool for adding two numbers.
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server instance
mcp = FastMCP("addition-server")

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: The first number
        b: The second number
    
    Returns:
        The sum of a and b
    """
    return a + b

@mcp.tool()
def add_multiple(numbers: list[float]) -> float:
    """
    Add multiple numbers together.
    
    Args:
        numbers: A list of numbers to add
    
    Returns:
        The sum of all provided numbers
    """
    return sum(numbers)

if __name__ == "__main__":
    # Run the server using stdio transport (default)
    # This is ideal for integration with tools like Claude Desktop or Cursor
    mcp.run(transport="stdio")