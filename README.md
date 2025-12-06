# thermo-mcp-server  
A minimal, easy-to-run **Model Context Protocol (MCP)** server that exposes temperature-related tools and demonstrates how external processes (thermometers, IoT devices, scripts, etc.) can write data that an MCP-enabled client can consume.

This project is intentionally small, readable, and built as a foundation for more advanced MCP tools.

---

## ⭐ Features

### ✔ Minimal FastMCP server  
Provides two MCP tools:

- `get_latest_temperature()` — Read the latest temperature JSON file  
- `set_latest_temperature()` — Write a new temperature value into the JSON file  

---

### ✔ External writer script  
`thermometer_listener.py` simulates a hardware thermometer by writing temperature data into the JSON file.  
This models how real-world devices or cron jobs feed data into MCP.

---

### ✔ Notifier module  
`notifier.py` outputs readable messages to stderr.  
You can extend this to integrate alerts, logs, webhooks, or push-notification systems.

---

### ✔ Cursor IDE Compatible  
Includes **optional `.cursor/` configuration** so Cursor MCP clients automatically detect and load the server.

---

## 📂 Project Structure

```
thermo-mcp-server/
│
├── server.py               # MCP server — exposes temperature tools
├── thermometer_listener.py # Simulated device that writes temperature JSON
├── notifier.py             # Simple stderr logger + threshold notifier
├── mcp_config.json         # Generic MCP config for MCP clients
├── requirements.txt        # Python deps (FastMCP + base libs)
│
├── data/
│   └── latest_temp.json    # Storage for temperature readings
│
└── .cursor/ (optional)
    └── commands/
        └── mcp.md          # Cursor MCP command helper
```

---

# 🚀 Quick Start (Terminal)

Run these **inside the repo folder**:

```bash
cd thermo-mcp-server
```

---

## 1. Create & activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Ensure the data folder exists

```bash
mkdir -p data
echo "{}" > data/latest_temp.json
```

---

# ▶ Running the MCP Server

Start the server:

```bash
python server.py
```

- In Cursor/ChatGPT/Claude Desktop: the MCP handshake begins automatically.  
- In Terminal: it waits for JSON-RPC (normal behavior).

---

# 🌡 Writing a Temperature

Simulate a thermometer reading:

```bash
python thermometer_listener.py --temp 72.5 --unit F
```

Example JSON written to `data/latest_temp.json`:

```json
{
  "temperature": 72.5,
  "unit": "F",
  "timestamp": "2025-12-06T04:36:52Z",
  "source": "listener"
}
```

Add a threshold alert:

```bash
python thermometer_listener.py --temp 90 --unit F --threshold 85
```

---

# 📁 Temperature File Format

The server reads/writes:

```
data/latest_temp.json
```

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

# 🧪 MCP Tools Exposed

### `get_latest_temperature() → dict`  
Returns the parsed JSON temperature data.

### `set_latest_temperature(value: float, unit: str = "F") → dict`  
Writes a new temperature entry (value + timestamp).

---

# 💻 Cursor Integration (Optional)

Cursor users can enable the MCP server automatically.

Files inside:

```
.cursor/
```

allow Cursor to discover and connect to the MCP server without manual setup.

---

# 🛠 Development Notes

- Code is intentionally simple and extensible  
- Ideal for experimenting with MCP  
- Easy to expand with:
  - device hardware  
  - push notifications  
  - cloud integrations  
  - automations  
- Safe to modify and fork  

---

# 🤝 Contributions

PRs welcome!  
Ideas:
- Additional MCP tools  
- IoT integrations  
- Notification pipelines  
- Improved examples  

---

# 📄 License

MIT License  
Free to use for learning, experimentation, and production.
