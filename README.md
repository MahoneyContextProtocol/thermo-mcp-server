# Cursor MCP Setup — thermo-mcp-server

This document explains how Cursor users can enable and interact with the `thermo-mcp-server` using Cursor’s builtin MCP support.

---

# 1. What the Server Provides Inside Cursor

Once enabled, Cursor exposes two MCP tools:

### ✔ `get_latest_temperature`  
Reads the most recent temperature entry.

### ✔ `set_latest_temperature`  
Writes a temperature value into the JSON file.

Cursor lists these tools under:  
**Settings → Tools & MCP → thermo-mcp-server**

---

# 2. Required Cursor MCP Configuration File

Cursor loads MCP definitions from:

```
<system_application_support_directory>/Cursor/mcp/
```

Create a file inside that directory (the location varies by OS):

```
thermo.json
```

Use this generic, path-agnostic configuration:

```json
{
  "command": "python",
  "args": ["server.py"],
  "workingDirectory": "<absolute-path-to-your-thermo-mcp-server-folder>",
  "env": {
    "THERMO_DATA_PATH": "data/latest_temp.json"
  }
}
```

**You must replace `<absolute-path-to-your-thermo-mcp-server-folder>`**  
with the real, full folder path on your system.

Examples (do NOT copy these literally):
- macOS: `/Users/<name>/Developer/thermo-mcp-server`
- Windows: `C:\\Users\\<name>\\Projects\\thermo-mcp-server`
- Linux: `/home/<user>/code/thermo-mcp-server`

---

# 3. Enabling the Server in Cursor

1. Open **Settings → Tools & MCP**
2. Find **thermo-mcp-server**
3. Toggle **Enable**

Cursor will attempt to launch:

```
python server.py
```

inside the working directory you provided.

If successful, Cursor will show:
- 🟢 Enabled  
- 🟢 Tools loaded (2 tools)

---

# 4. Using MCP Tools Inside Cursor Chat

In any Cursor chat, type:

```
@get_latest_temperature
```

or:

```
@set_latest_temperature value=72.5 unit=F
```

Cursor will autocomplete MCP tools and run them.

---

# 5. Troubleshooting

### ❌ Server shows JSON errors  
The configuration file (`thermo.json`) probably contains invalid JSON.

### ❌ File not found errors  
Check that:
- The workingDirectory is correct  
- `data/latest_temp.json` exists  
- The virtual environment is set up  

### ❌ Python not found  
Configure Python path in:  
**Settings → Agents → Python interpreter**

### ❌ Server exits immediately  
That's normal if run manually in Terminal — only MCP clients speak JSON-RPC.

---

# 6. Development Workflow for Cursor Users

1. Edit the Python code  
2. If the server is enabled, Cursor will detect changes when you toggle it  
3. Turn the server OFF → ON to reload  
4. Use **View → Debug Console → MCP** to view logs

---

# End of Cursor Documentation
