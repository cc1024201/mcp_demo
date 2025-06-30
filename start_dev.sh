#!/bin/bash
# 开发模式启动脚本
echo "启动 MCP 服务器开发模式..."
echo "这将在浏览器中打开一个交互式界面"
echo ""

# 激活虚拟环境
source venv/bin/activate

# 启动开发服务器
mcp dev addition_server.py