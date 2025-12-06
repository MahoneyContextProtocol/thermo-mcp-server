# thermo-mcp-server  
A minimal, example-friendly **Model Context Protocol (MCP)** server that exposes temperature tools and demonstrates how external processes can update data for MCP-enabled clients.

This project is intentionally tiny, readable, and designed as a foundation for learning MCP or building your own tools and integrations.

---

# 📦 Features

### ✔ FastMCP-based server  
Exposes two simple MCP tools:
- `get_latest_temperature()` — Reads the latest temperature JSON  
- `set_latest_temperature()` — Writes a new value into the JSON file  

### ✔ External sensor simulator  
`thermometer_listener.py` simulates an IoT device writing temperature data.

### ✔ Simple notifier  
`notifier.py` outputs messages to stderr, including threshold alerts.

### ✔ Optional Cursor IDE integration  
Includes optional MCP client configuration under `.cursor/`.

---

# 🗂 Project Structure

```
thermo-mcp-server/
│
├── server.py               # MCP server entrypoint
├── thermometer_listener.py # CLI that writes temperature data
├── notifier.py             # Threshold + stderr logger
├── mcp_config.json         # Standard JSON config used by many MCP clients
├── requirements.txt        # Python dependencies
│
├── data/
│   └── latest_temp.json    # Where readings are stored
│
└── .cursor/                # (optional) Cursor MCP client config
    └── commands/
        └── mcp.md
```

---

# 🚀 Quick Start (Terminal)

Run these commands from inside the project directory:

## 1. Create & activate the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Create the data directory

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

If you're using an MCP-enabled client (Cursor / ChatGPT / Claude Desktop),  
it will automatically communicate with the server through stdin/stdout.

Running it directly in Terminal will show no output — this is normal because  
JSON-RPC clients send structured messages that a human normally doesn’t type.

---

# 🌡 Writing a Temperature (Simulated Device)

```bash
python thermometer_listener.py --temp 72.5 --unit F
```

This will:

1. Write into `data/latest_temp.json`
2. Log a message to stderr
3. Optionally trigger a threshold warning:

```bash
python thermometer_listener.py --temp 90 --unit F --threshold 85
```

---

# 📁 Temperature File Format

Example `data/latest_temp.json`:

```json
{
  "temperature": 72.5,
  "unit": "F",
  "timestamp": "2025-12-06T00:00:00Z",
  "source": "listener"
}
```

---

# 🧪 MCP Tools Provided

### `get_latest_temperature()`
Returns the parsed contents of the temperature file.

### `set_latest_temperature(value, unit="F")`
Writes a new temperature value and timestamp.

---

# 💻 Cursor Integration (Optional)

Cursor-specific instructions live inside:

```
.cursor/commands/mcp.md
```

This enables Cursor to discover and load the MCP server automatically.

---

# 🤝 Contributions
Contributions are welcome — improvements to documentation, new MCP tools,  
better examples, expanded device simulators, and more are encouraged.

---

# 📄 License
MIT License.
