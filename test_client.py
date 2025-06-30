#!/usr/bin/env python3
"""
MCP 客户端测试示例
用于测试 addition_server.py 的功能
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # 创建服务器参数，指向我们的 MCP 服务器
    server_params = StdioServerParameters(
        command="python",
        args=["addition_server.py"],
        env=None
    )
    
    # 使用 stdio 客户端连接到服务器
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化会话
            await session.initialize()
            
            # 列出所有可用的工具
            print("可用的工具:")
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")
            
            print("\n测试 add_numbers 工具:")
            # 调用 add_numbers 工具
            result1 = await session.call_tool(
                "add_numbers",
                arguments={"a": 5, "b": 3}
            )
            print(f"5 + 3 = {result1.content[0].text}")
            
            # 测试浮点数
            result2 = await session.call_tool(
                "add_numbers",
                arguments={"a": 3.14, "b": 2.86}
            )
            print(f"3.14 + 2.86 = {result2.content[0].text}")
            
            print("\n测试 add_multiple 工具:")
            # 调用 add_multiple 工具 - 注意：*args 参数需要分别传递
            result3 = await session.call_tool(
                "add_multiple",
                arguments={"numbers": [1, 2, 3, 4, 5]}
            )
            print(f"1 + 2 + 3 + 4 + 5 = {result3.content[0].text}")

if __name__ == "__main__":
    asyncio.run(main())