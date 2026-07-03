import numpy as np

from loudspeaker_modeling.dsp.preprocessing import estimate_lag, peak_normalize, segment_signal


def test_peak_normalize_scales_to_requested_peak():
    signal = np.array([0.0, 2.0, -4.0])
    normalized = peak_normalize(signal, peak=0.5)
    assert np.max(np.abs(normalized)) == 0.5


def test_segment_signal_returns_expected_windows():
    signal = np.arange(6)
    segments = segment_signal(signal, segment_length=3, hop_length=2)
    assert segments.tolist() == [[0, 1, 2], [2, 3, 4]]


def test_estimate_lag_detects_delay():
    reference = np.array([0, 1, 0, 0, 0], dtype=float)
    measured = np.array([0, 0, 0, 1, 0], dtype=float)
    assert estimate_lag(reference, measured, max_lag=3) == 2
