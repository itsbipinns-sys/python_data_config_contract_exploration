from typing import Dict
from pydantic import BaseModel, ValidationError, Field
from .utils.config_loader import load_json_config

class JobConfigModel(BaseModel):
    input_path: str
    output_path: str
    batch_size: int = 100

class JobConfigAliasModel(BaseModel):
    input_path: str = Field(..., alias="x")
    output_path: str = Field(..., alias="y")
    batch_size: int = Field(100, alias="z")

def run_pydantic_job(config_path: str) -> Dict[str, str]:
    raw = load_json_config(config_path)
    # If the input is known to have mismatched keys (e.g., x, y, z), use the alias model
    if set(raw.keys()) >= {"x", "y", "z"}:
        model = JobConfigAliasModel
    else:
        model = JobConfigModel
    try:
        cfg = model(**raw)
    except ValidationError as e:
        print("Validation failed:", e)
        raise
    result = {
        "read": cfg.input_path,
        "write": cfg.output_path,
        "batch": str(cfg.batch_size),
    }
    print("Pydantic job running with:", result)
    return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m config_compare.pydantic_job <config.json>")
    else:
        run_pydantic_job(sys.argv[1])
