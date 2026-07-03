from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv


REQUIRED_COLUMNS = [
    "recording_id",
    "file_path",
    "speaker_id",
    "signal_type",
    "level_dbfs",
    "repetition",
    "sample_rate_hz",
    "input_channel",
    "microphone_channel",
]


@dataclass(frozen=True)
class Recording:
    recording_id: str
    file_path: str
    speaker_id: str
    signal_type: str
    level_dbfs: float
    repetition: int
    sample_rate_hz: int
    input_channel: int
    microphone_channel: int


def read_manifest(path: str | Path) -> list[Recording]:
    manifest_path = Path(path)
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")

    with manifest_path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        validate_columns(reader.fieldnames or [])
        return [
            Recording(
                recording_id=row["recording_id"],
                file_path=row["file_path"],
                speaker_id=row["speaker_id"],
                signal_type=row["signal_type"],
                level_dbfs=float(row["level_dbfs"]),
                repetition=int(row["repetition"]),
                sample_rate_hz=int(row["sample_rate_hz"]),
                input_channel=int(row["input_channel"]),
                microphone_channel=int(row["microphone_channel"]),
            )
            for row in reader
            if any(value.strip() for value in row.values() if value is not None)
        ]


def validate_columns(columns: list[str]) -> None:
    missing = [column for column in REQUIRED_COLUMNS if column not in columns]
    if missing:
        raise ValueError(f"Manifest is missing required columns: {', '.join(missing)}")
