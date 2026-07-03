from __future__ import annotations

import argparse
from pathlib import Path

from _bootstrap import add_src_to_path

add_src_to_path()

from loudspeaker_modeling.data.manifest import read_manifest
from loudspeaker_modeling.utils.config import load_yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Preprocess raw loudspeaker measurements.")
    parser.add_argument("--params", default="params.yaml")
    args = parser.parse_args()

    config = load_yaml(args.params)
    manifest_path = Path(config["paths"]["raw_manifest"])
    recordings = read_manifest(manifest_path)
    output_dir = Path(config["paths"]["processed_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Validated {len(recordings)} manifest rows. Preprocessing implementation is pending.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
