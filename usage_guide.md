# MCP 服务器使用指南

## 使用方式

MCP 服务器有三种主要使用方式：

### 1. 直接运行测试客户端

在激活虚拟环境后，运行测试客户端：

```bash
source venv/bin/activate
python test_client.py
```

这会连接到 MCP 服务器并演示如何调用加法工具。

### 2. 集成到 Claude Desktop

1. 找到 Claude Desktop 配置文件：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. 编辑配置文件，添加：
```json
{
  "mcpServers": {
    "addition-server": {
      "command": "/home/zhcao/mcp_demo/venv/bin/python",
      "args": ["/home/zhcao/mcp_demo/addition_server.py"]
    }
  }
}
```

3. 重启 Claude Desktop

4. 在 Claude 中使用：
   - "使用 add_numbers 计算 10 + 20"
   - "使用 add_multiple 计算 1, 2, 3, 4, 5 的总和"

### 3. 开发模式（用于调试）

如果你想在浏览器中交互式测试：

```bash
source venv/bin/activate
cd /home/zhcao/mcp_demo
# 安装开发工具
pip install "mcp[cli]"
# 启动开发服务器
mcp dev addition_server.py
```

然后在浏览器中访问显示的 URL（通常是 http://localhost:5173）。

## MCP 工作原理

1. **服务器端**：MCP 服务器（addition_server.py）暴露工具供客户端调用
2. **传输协议**：使用 stdio（标准输入/输出）进行通信
3. **客户端**：可以是 Claude Desktop、测试脚本或其他支持 MCP 的应用

## 工具说明

- `add_numbers(a, b)`: 计算两个数的和
- `add_multiple(*numbers)`: 计算多个数的和

## 常见问题

1. **无法连接到服务器**：确保虚拟环境已激活并且依赖已安装
2. **Claude Desktop 找不到工具**：检查配置文件路径是否正确，并重启 Claude Desktop
3. **权限错误**：确保 Python 脚本有执行权限