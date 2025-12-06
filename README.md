
# thermo-mcp-server — Cursor Support Edition  
This branch provides **Cursor-optimized MCP configuration**, making it effortless for Cursor IDE users to run, connect, and use the server with zero manual setup.

It includes everything from the main branch plus Cursor-specific files, workflows, and setup instructions.

---

# 🎯 What This Branch Adds

### ✔ Automatic MCP Detection in Cursor  
Includes:  
```
.cursor/mcp_thermo.json
.cursor/commands/mcp.md
```
These allow Cursor to discover and register the MCP server immediately.

### ✔ Ready-to-run FastMCP Server  
No changes to functionality — still exposes:

- `get_latest_temperature()`  
- `set_latest_temperature()`  

### ✔ Easy Device Simulation  
Cursor users can write temperatures via:

```bash
python thermometer_listener.py --temp 72.5 --unit F
```

### ✔ Same JSON temperature storage  
Shared file:

```
data/latest_temp.json
```

---

# 🗂 Project Structure (Cursor Edition)

```
thermo-mcp-server/
│
├── server.py
├── thermometer_listener.py
├── notifier.py
├── mcp_config.json
├── requirements.txt
│
├── data/
│   └── latest_temp.json
│
└── .cursor/
    ├── mcp_thermo.json          # Cursor MCP server registration
    └── commands/
        └── mcp.md               # Optional helper command
```

---

# 🚀 Quick Start (Cursor Users)

Follow these steps **inside Cursor**:

## 1. Open a Terminal in Cursor

Use:

```
Ctrl/Cmd + `
```

Then run:

```bash
cd thermo-mcp-server
```

---

## 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install requirements

```bash
pip install -r requirements.txt
```

Expected Cursor terminal output:

- All packages install successfully  
- No warnings that stop execution  
- MCP server dependencies installed  

---

## 4. Run the MCP server *inside Cursor*

```bash
python server.py
```

Cursor will automatically show:

- ✔ Server detected  
- ✔ Tools loading  
- ✔ thermo-mcp-server connected  

You do **not** need to run `/mcp` — Cursor handles everything.

---

# 🌡 Writing a Temperature (Inside Cursor Terminal)

```bash
python thermometer_listener.py --temp 73.2 --unit F
```

Check the JSON:

```bash
cat data/latest_temp.json
```

Cursor's MCP tools can now call:

- `get_latest_temperature`
- `set_latest_temperature`

directly from the chat.

---

# 📄 Temperature JSON Format

```
{
  "temperature": 73.2,
  "unit": "F",
  "timestamp": "2025-12-06T04:36:52Z",
  "source": "listener"
}
```

---

# 💻 Cursor MCP Files Included

### `.cursor/mcp_thermo.json`

Tells Cursor:

- how to start the server  
- where the working directory is  
- how to pass environment variables  

### `.cursor/commands/mcp.md`

Provides:

- helper text  
- examples  
- links for users  

---

# 🛠 Notes for Cursor Users

- The server automatically streams logs to the Cursor "MCP Tools" sidebar.  
- Each tool includes hoverable JSON schemas.  
- Cursor automatically reloads the MCP service when you edit `server.py`.  
- Cursor users can extend the MCP server with new tools without restarting the IDE.

---

# 🤝 Contributions (Cursor Edition)

Ideas welcome:

- Cursor autocomplete plugins  
- Temperature dashboards  
- Push-notification integrations  
- IoT device bridges  

---

# 📄 License

MIT License  
Use freely inside or outside Cursor.
