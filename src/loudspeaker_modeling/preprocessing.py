from __future__ import annotations

from pathlib import Path
from typing import Any
import json

import yaml


def load_params(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def prepare_processed_dir(path: str | Path) -> Path:
    processed_dir = Path(path)
    processed_dir.mkdir(parents=True, exist_ok=True)
    return processed_dir


def summarize_raw_dir(path: str | Path) -> dict[str, Any]:
    raw_dir = Path(path)
    raw_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(file for file in raw_dir.iterdir() if file.is_file() and file.name != ".gitkeep")
    return {
        "raw_dir": str(raw_dir),
        "file_count": len(files),
        "files": [file.name for file in files],
    }


def write_preprocessing_summary(
    processed_dir: str | Path,
    raw_summary: dict[str, Any],
    params: dict[str, Any],
) -> Path:
    output_path = Path(processed_dir) / "preprocessing_summary.json"
    summary = {
        "status": "no_preprocessing_method_selected",
        "raw_data": raw_summary,
        "preprocessing": params.get("preprocessing", {}),
    }
    output_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return output_path
