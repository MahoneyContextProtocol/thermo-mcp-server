# thermo-mcp-server

Minimal Model Context Protocol (MCP) server exposing temperature tools.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python server.py

python thermometer_listener.py --temp 72.5 --unit F

python thermometer_listener.py --temp 72.5 --unit F


---

### 📄 `data/latest_temp.json`

```bash
cat > data/latest_temp.json << 'EOF'
{}
