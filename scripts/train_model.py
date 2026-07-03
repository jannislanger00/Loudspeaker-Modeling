from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from loudspeaker_modeling.model import load_params


def main() -> int:
    parser = argparse.ArgumentParser(description="Train the selected model.")
    parser.add_argument("--params", default="params.yaml")
    args = parser.parse_args()

    params = load_params(args.params)
    model_name = params["model"].get("name")
    if model_name is None:
        print("No model selected yet. Set model.name in params.yaml after deciding the model.")
        return 0
    print(f"Selected model: {model_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
