# thermo-mcp-server  
A minimal, easy-to-run **Model Context Protocol (MCP)** server that exposes temperature-related tools and demonstrates how external processes (thermometers, IoT devices, scripts, etc.) can write data that an MCP-enabled client can consume.

This project is intentionally small, readable, and designed as a foundation for building more advanced MCP tools.

---

# 📦 Features

### ✔ Minimal FastMCP server  
Provides two MCP tools:
- `get_latest_temperature()` — Read the latest temperature JSON file  
- `set_latest_temperature()` — Write a new temperature value into the JSON file  

### ✔ External writer script  
A CLI tool (`thermometer_listener.py`) simulates a thermometer sending readings to the MCP server by writing directly to the JSON file. This allows testing real-world workflows where hardware feeds MCP.

### ✔ Notifier module  
A tiny utility (`notifier.py`) that writes human-readable messages to stderr. This can be extended to integrate with alerts, logs, or UI notifications.

### ✔ Cursor IDE Compatible  
Includes optional configuration files for Cursor MCP clients.

---

# 🗂 Project Structure

```
thermo-mcp-server/
│
├── server.py               # MCP server — exposes temperature tools
├── thermometer_listener.py # Simulated device that writes temperature JSON
├── notifier.py             # Simple stderr logger + threshold notifier
├── mcp_config.json         # Generic MCP config used by multiple clients
├── requirements.txt        # Python requirements (FastMCP + dependencies)
│
├── data/
│   └── latest_temp.json    # Where temperature readings are stored
│
└── .cursor/                # (optional) Cursor MCP config & commands
    └── commands/
        └── mcp.md
```

---

# 🚀 Quick Start (Terminal)

These commands must be run **from inside the repo directory**:

```bash
cd ~/Developer/thermo-mcp-server
```

## 1. Create & activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Ensure the `data` directory exists

```bash
mkdir -p data
echo "{}" > data/latest_temp.json
```

---

# ▶ Running the MCP Server

Once dependencies are installed:

```bash
python server.py
```

If you're running this inside an MCP client (Cursor/ChatGPT/Claude Desktop),  
the MCP handshake will begin automatically.

If running in Terminal, the server will wait for JSON-RPC messages (normal behavior).

---

# 🌡 Writing a Temperature (Simulated Thermometer)

Use the CLI writer to simulate an external sensor:

```bash
python thermometer_listener.py --temp 72.5 --unit F
```

This will:

1. Write the JSON below:

```json
{
  "temperature": 72.5,
  "unit": "F",
  "timestamp": "2025-12-06T04:36:52Z",
  "source": "listener"
}
```

2. Print messages to stderr  
3. Trigger threshold alerts if provided:

```bash
python thermometer_listener.py --temp 90 --unit F --threshold 85
```

---

# 📁 Temperature File Format

The server and listener both read/write:

`data/latest_temp.json`

Example:

```json
{
  "temperature": 70.0,
  "unit": "F",
  "timestamp": "2025-12-06T04:00:00Z",
  "source": "listener"
}
```

---

# 🧪 MCP Tools Exposed by the Server

### `get_latest_temperature() → dict`
Returns the parsed JSON from `data/latest_temp.json`.

### `set_latest_temperature(value: float, unit: str = "F") → dict`
Writes a new value and timestamp into the file.

---

# 💻 Cursor Integration (Optional)

Cursor-specific instructions live inside:

```
.cursor/commands/mcp.md
```

This enables Cursor to automatically discover and interact with the MCP server.

---

# 🛠 Development Notes

- Code aims to be readable and modifiable  
- No frameworks beyond MCP dependencies  
- Designed for rapid experimentation with MCP tooling  
- Safe to extend with websockets, hardware integration, databases, etc.

---

# 🤝 Contributions

PRs and suggestions are welcome, especially:
- Adding more MCP tools  
- Hardware integrations  
- Cursor workflows  
- Better UX for MCP beginners  

---

# 📄 License

MIT License.  
Use freely for learning, experimentation, and production.
