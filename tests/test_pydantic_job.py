import json
from config_compare.pydantic_job import run_pydantic_job

def test_pydantic_job(tmp_path):
    cfg = {"input_path": "in.json", "output_path": "out.json", "batch_size": 25}
    p = tmp_path / "cfg.json"
    p.write_text(json.dumps(cfg))
    res = run_pydantic_job(str(p))
    assert res["read"] == "in.json"
    assert res["write"] == "out.json"
    assert res["batch"] == "25"
