from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import add_src_to_path

add_src_to_path()

from loudspeaker_modeling.utils.config import load_yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate loudspeaker models.")
    parser.add_argument("--params", default="params.yaml")
    args = parser.parse_args()

    config = load_yaml(args.params)
    metrics_dir = Path(config["paths"]["artifacts_dir"]) / "metrics"
    metrics_dir.mkdir(parents=True, exist_ok=True)
    summary_path = metrics_dir / "evaluation_summary.json"
    summary = {
        "status": "pending_data",
        "message": "Evaluation pipeline is scaffolded; add processed data and trained models next.",
    }
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
