import json
import os
from datetime import datetime
from pathlib import Path

from mcp.server.fastmcp import FastMCP

APP_NAME = "thermo-mcp-server"
DATA_PATH = Path(os.environ.get("THERMO_DATA_PATH", "data/latest_temp.json"))

app = FastMCP(APP_NAME)


def _read_latest() -> dict:
    try:
        with DATA_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _write_latest(temp: float, unit: str = "F", source: str = "mcp") -> dict:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "temperature": float(temp),
        "unit": unit,
        "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "source": source,
    }
    with DATA_PATH.open("w", encoding="utf-8") as f:
        json.dump(payload, f)
    return payload


@app.tool()
def get_latest_temperature() -> dict:
    return _read_latest()


@app.tool()
def set_latest_temperature(value: float, unit: str = "F") -> dict:
    return _write_latest(value, unit=unit, source="mcp")


if __name__ == "__main__":
    app.run()
