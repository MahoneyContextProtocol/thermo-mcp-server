import sys

def notify(message: str) -> None:
    print(message, file=sys.stderr)

def notify_if_threshold(value: float, threshold: float) -> None:
    if value >= threshold:
        notify(f"Threshold reached: {value} >= {threshold}")
