import json
from pathlib import Path
from typing import Any


def to_pretty_json(data: dict[str, Any]) -> str:
    return json.dumps(data, indent=4, ensure_ascii=False)


def save_json_report(data: dict[str, Any], output_path: str) -> str:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(to_pretty_json(data), encoding="utf-8")
    return str(path)