import json
from typing import Any, Dict

def load_json_config(path: str) -> Dict[str, Any]:
    """Load a JSON file and return as dict."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
