# MCP Addition Server

一个简单的 MCP (Model Context Protocol) 服务器示例，提供两数相加的功能。

## 功能

这个 MCP 服务器提供了两个工具：
1. `add_numbers` - 将两个数字相加
2. `add_multiple` - 将多个数字相加

## 安装

1. 创建虚拟环境（推荐）：
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或者在 Windows 上：venv\Scripts\activate
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 运行服务器

```bash
python addition_server.py
```

服务器默认使用 stdio 传输协议运行，适合与 Claude Desktop、Cursor 等工具集成。

## 集成到 Claude Desktop

1. 找到 Claude Desktop 的配置文件：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. 编辑配置文件，添加服务器：
```json
{
  "mcpServers": {
    "addition-server": {
      "command": "python",
      "args": ["/path/to/addition_server.py"]
    }
  }
}
```

3. 重启 Claude Desktop

## 使用示例

在 Claude Desktop 中，你可以这样使用：
- "使用 add_numbers 工具计算 5 + 3"
- "使用 add_multiple 工具计算 1, 2, 3, 4, 5 的和"

## 开发模式

如果你想在开发模式下测试服务器：
```bash
# 如果安装了 mcp[cli]
mcp dev
```

这将启动一个开发服务器，你可以在浏览器中查看和测试你的工具。