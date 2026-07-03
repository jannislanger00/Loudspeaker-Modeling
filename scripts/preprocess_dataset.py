from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from loudspeaker_modeling.preprocessing import load_params
from loudspeaker_modeling.preprocessing import prepare_processed_dir
from loudspeaker_modeling.preprocessing import summarize_raw_dir
from loudspeaker_modeling.preprocessing import write_preprocessing_summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the selected preprocessing step.")
    parser.add_argument("--params", default="params.yaml")
    args = parser.parse_args()

    params = load_params(args.params)
    raw_summary = summarize_raw_dir(params["paths"]["raw_dir"])
    processed_dir = prepare_processed_dir(params["paths"]["processed_dir"])
    summary_path = write_preprocessing_summary(processed_dir, raw_summary, params)
    print(f"Wrote preprocessing summary: {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
