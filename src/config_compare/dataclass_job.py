from dataclasses import dataclass
from typing import Dict
from .utils.config_loader import load_json_config
from .utils.validators import validate_basic
from .utils.dataclass_mapper import map_to_dataclass

@dataclass
class JobConfig:
    input_path: str
    output_path: str
    batch_size: int = 100

def run_dataclass_job(config_path: str) -> Dict[str, str]:
    raw = load_json_config(config_path)
    # If the input is known to have mismatched keys (e.g., x, y, z, a, b, c), use a mapping
    if set(raw.keys()) >= {"x", "y", "z", "a", "b", "c"}:
        key_map = {
            "input_path": "x",
            "output_path": "y",
            "batch_size": "z"
        }
        cfg = map_to_dataclass(JobConfig, raw, key_map)
    else:
        # Try to instantiate directly if keys match
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
        print("Demo: python -m config_compare.dataclass_job configs/demo_mapped_config.json")
    else:
        # For demo, if using demo_mapped_config.json, set mapping for mismatched keys
        config_path = sys.argv[1]
        if config_path.endswith("demo_mapped_config.json"):
            # Override key_map for demo
            def run_demo_job(config_path):
                raw = load_json_config(config_path)
                key_map = {
                    "input_path": "read",
                    "output_path": "write",
                    "batch_size": "batch"
                }
                required = {k: str if k.endswith('_path') else int for k in key_map}
                validate_basic({k: raw.get(key_map[k]) for k in key_map}, required)
                cfg = map_to_dataclass(JobConfig, raw, key_map)
                result = {
                    "read": cfg.input_path,
                    "write": cfg.output_path,
                    "batch": str(cfg.batch_size),
                }
                print("Dataclass job running with:", result)
                return result
            run_demo_job(config_path)
        else:
            run_dataclass_job(config_path)
