from __future__ import annotations

import numpy as np


def peak_normalize(signal: np.ndarray, peak: float = 0.95) -> np.ndarray:
    if peak <= 0:
        raise ValueError("peak must be positive")
    max_abs = float(np.max(np.abs(signal))) if signal.size else 0.0
    if max_abs == 0.0:
        return signal.copy()
    return signal * (peak / max_abs)


def segment_signal(signal: np.ndarray, segment_length: int, hop_length: int) -> np.ndarray:
    if segment_length <= 0 or hop_length <= 0:
        raise ValueError("segment_length and hop_length must be positive")
    if signal.ndim != 1:
        raise ValueError("segment_signal expects a one-dimensional signal")
    if signal.size < segment_length:
        return np.empty((0, segment_length), dtype=signal.dtype)
    starts = range(0, signal.size - segment_length + 1, hop_length)
    return np.stack([signal[start : start + segment_length] for start in starts])


def estimate_lag(reference: np.ndarray, measured: np.ndarray, max_lag: int) -> int:
    if reference.ndim != 1 or measured.ndim != 1:
        raise ValueError("estimate_lag expects one-dimensional signals")
    if max_lag < 0:
        raise ValueError("max_lag must be non-negative")

    corr = np.correlate(measured, reference, mode="full")
    center = reference.size - 1
    start = max(center - max_lag, 0)
    stop = min(center + max_lag + 1, corr.size)
    return int(np.argmax(corr[start:stop]) + start - center)
