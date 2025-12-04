from typing import Dict, Any

def validate_basic(config: Dict[str, Any], required: Dict[str, type]) -> bool:
    """Simple validator that checks required keys and types."""
    for key, tp in required.items():
        if key not in config:
            raise KeyError(f"Missing required key: {key}")
        if not isinstance(config[key], tp):
            raise TypeError(f"Key '{key}' expected type {tp.__name__}, got {type(config[key]).__name__}")
    return True
