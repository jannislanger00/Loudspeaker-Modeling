from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_params(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def no_model_selected_message() -> str:
    return "No model has been selected yet."
