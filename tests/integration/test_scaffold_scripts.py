import json
import subprocess
import sys
from pathlib import Path


def test_evaluate_script_writes_pending_summary():
    result = subprocess.run(
        [sys.executable, "scripts/evaluate_model.py", "--params", "params.yaml"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "evaluation_summary.json" in result.stdout
    summary = json.loads(Path("artifacts/metrics/evaluation_summary.json").read_text())
    assert summary["status"] == "pending_data"
