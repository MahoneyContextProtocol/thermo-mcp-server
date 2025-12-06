import argparse
import json
from datetime import datetime
from pathlib import Path

from notifier import notify, notify_if_threshold

DATA_PATH = Path("data/latest_temp.json")


def write_reading(temp: float, unit: str = "F", source: str = "listener") -> dict:
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


def main():
    parser = argparse.ArgumentParser(description="Record a thermometer reading")
    parser.add_argument("--temp", type=float, required=True)
    parser.add_argument("--unit", type=str, default="F", choices=["F", "C"])
    parser.add_argument("--threshold", type=float)
    args = parser.parse_args()

    payload = write_reading(args.temp, unit=args.unit)

    if args.threshold is not None:
        notify_if_threshold(args.temp, args.threshold)

    notify(f"Recorded temperature: {payload}")


if __name__ == "__main__":
    main()
