# Cursor MCP Setup — thermo-mcp-server

This document explains **exactly how Cursor users can run and interact with the thermo MCP server**, including installation, activation, troubleshooting, and expected tool behavior.

---

# 1. What This Server Does in Cursor

Once activated, Cursor will automatically detect the MCP server and expose two tools:

### ✔ `get_latest_temperature`  
Read the most recent temperature JSON entry.

### ✔ `set_latest_temperature`  
Write a new value into the temperature JSON file.

Cursor will show these tools inside:  
**Settings → Tools & MCP → thermo-mcp-server**

---

# 2. Folder Locations Required by Cursor

Cursor expects MCP configurations in:

```
~/Library/Application Support/Cursor/mcp/
```

Your configuration file should be named:

```
thermo.json
```

And its contents should be:

```json
{
  "command": "python",
  "args": ["server.py"],
  "workingDirectory": "/Users/joemahoney/Developer/thermo-mcp-server",
  "env": {
    "THERMO_DATA_PATH": "data/latest_temp.json"
  }
}
```

Be sure that:

- The workingDirectory path matches your local repo path  
- The JSON file is valid  
- Cursor is restarted after adding this file  

---

# 3. How to Enable the Server in Cursor

### Step 1 — Open Cursor Settings  
Go to:

**Settings → Tools & MCP**

Scroll until you find:

**thermo-mcp-server → Enable toggle**

Turn it **ON**.

Cursor will automatically attempt to start:

```
python server.py
```

behind the scenes using your local environment.

---

# 4. Verifying the Server is Running

When successful, Cursor will show:

- 🟢 **Enabled**  
- 🟢 **Tools loaded**  
- 2 tools listed under the server  

If the server fails, Cursor will display errors in red.

Troubleshooting hints:

### If Python not found:
Set Cursor’s Python path manually:

**Settings → Agents → Runtime → Python interpreter**

### If MCP handshake fails:
Usually caused by invalid JSON in `thermo.json`.

### If server reports EOF errors:
This is normal when running the server manually in Terminal —  
Cursor is the only environment that will speak JSON-RPC correctly.

---

# 5. Using the Tools Inside Cursor Chat

Inside any Cursor chat:

Type:

```
@get_latest_temperature
```

or

```
@set_latest_temperature value=72.5 unit=F
```

Cursor will autocomplete MCP tools and call the functions automatically.

---

# 6. Development Workflow for Cursor Users

1. Edit the python files normally  
2. Cursor-hot reload does not apply; restart the MCP server:  
   Turn the toggle OFF → ON  
3. Watch logs using:  
   **View → Debug Console → MCP**

---

# 7. Notes for Contributors

- Cursor users should work on `cursor-support` branch  
- `.cursor/` folder is optional for non-Cursor users  
- MCP configs should always be JSON-validated  
