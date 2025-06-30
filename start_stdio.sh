#!/bin/bash
# 直接运行 MCP 服务器（stdio 模式）
echo "启动 MCP 服务器 (stdio 模式)..."
echo "服务器将等待客户端连接"
echo "按 Ctrl+C 停止服务器"
echo ""

# 激活虚拟环境并运行
source venv/bin/activate
python addition_server.py