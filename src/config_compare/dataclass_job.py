from dataclasses import dataclass
from typing import Dict
from .utils.config_loader import load_json_config
from .utils.validators import validate_basic

@dataclass
class JobConfig:
    input_path: str
    output_path: str
    batch_size: int = 100

def run_dataclass_job(config_path: str) -> Dict[str, str]:
    raw = load_json_config(config_path)
    required = {"input_path": str, "output_path": str, "batch_size": int}
    validate_basic(raw, required)
    cfg = JobConfig(**raw)
    result = {
        "read": cfg.input_path,
        "write": cfg.output_path,
        "batch": str(cfg.batch_size),
    }
    print("Dataclass job running with:", result)
    return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m config_compare.dataclass_job <config.json>")
    else:
        run_dataclass_job(sys.argv[1])
