from pathlib import Path

from loudspeaker_modeling.preprocessing import prepare_processed_dir
from loudspeaker_modeling.preprocessing import summarize_raw_dir
from loudspeaker_modeling.preprocessing import write_preprocessing_summary


def test_preprocessing_summary_is_deterministic(tmp_path: Path):
    raw_dir = tmp_path / "raw"
    processed_dir = tmp_path / "processed"
    raw_dir.mkdir()
    (raw_dir / "b.wav").write_text("", encoding="utf-8")
    (raw_dir / "a.wav").write_text("", encoding="utf-8")

    prepared_dir = prepare_processed_dir(processed_dir)
    raw_summary = summarize_raw_dir(raw_dir)
    summary_path = write_preprocessing_summary(
        prepared_dir,
        raw_summary,
        {"preprocessing": {"enabled": False, "method": None}},
    )

    assert raw_summary["files"] == ["a.wav", "b.wav"]
    assert summary_path.exists()
