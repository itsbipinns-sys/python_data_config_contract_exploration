import json
from config_compare.dataclass_job import run_dataclass_job

def test_dataclass_job(tmp_path):
    cfg = {"input_path": "in.json", "output_path": "out.json", "batch_size": 50}
    p = tmp_path / "cfg.json"
    p.write_text(json.dumps(cfg))
    res = run_dataclass_job(str(p))
    assert res["read"] == "in.json"
    assert res["write"] == "out.json"
    assert res["batch"] == "50"
