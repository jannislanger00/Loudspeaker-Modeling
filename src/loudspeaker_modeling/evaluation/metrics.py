from __future__ import annotations

import numpy as np


def mse(reference: np.ndarray, estimate: np.ndarray) -> float:
    reference, estimate = _paired(reference, estimate)
    return float(np.mean((reference - estimate) ** 2))


def esr(reference: np.ndarray, estimate: np.ndarray, eps: float = 1e-12) -> float:
    reference, estimate = _paired(reference, estimate)
    error_energy = np.sum((reference - estimate) ** 2)
    signal_energy = np.sum(reference**2)
    return float(error_energy / max(signal_energy, eps))


def esr_db(reference: np.ndarray, estimate: np.ndarray, eps: float = 1e-12) -> float:
    return float(10.0 * np.log10(max(esr(reference, estimate, eps), eps)))


def stft_magnitude_error(
    reference: np.ndarray,
    estimate: np.ndarray,
    n_fft: int = 2048,
    hop_length: int = 512,
    eps: float = 1e-12,
) -> float:
    reference, estimate = _paired(reference, estimate)
    ref_spec = _stft_mag(reference, n_fft, hop_length)
    est_spec = _stft_mag(estimate, n_fft, hop_length)
    return float(np.mean(np.abs(20 * np.log10(ref_spec + eps) - 20 * np.log10(est_spec + eps))))


def thd(signal: np.ndarray, sample_rate_hz: int, fundamental_hz: float, max_harmonic: int = 5) -> float:
    if fundamental_hz <= 0:
        raise ValueError("fundamental_hz must be positive")
    spectrum = np.abs(np.fft.rfft(signal))
    freqs = np.fft.rfftfreq(signal.size, d=1.0 / sample_rate_hz)
    fundamental = _bin_amplitude(spectrum, freqs, fundamental_hz)
    harmonic_energy = 0.0
    for order in range(2, max_harmonic + 1):
        freq = fundamental_hz * order
        if freq >= sample_rate_hz / 2:
            break
        harmonic_energy += _bin_amplitude(spectrum, freqs, freq) ** 2
    return float(np.sqrt(harmonic_energy) / max(fundamental, 1e-12))


def imd_two_tone(
    signal: np.ndarray,
    sample_rate_hz: int,
    f1_hz: float,
    f2_hz: float,
    max_order: int = 3,
) -> float:
    if f1_hz <= 0 or f2_hz <= 0 or f1_hz == f2_hz:
        raise ValueError("f1_hz and f2_hz must be distinct positive frequencies")
    spectrum = np.abs(np.fft.rfft(signal))
    freqs = np.fft.rfftfreq(signal.size, d=1.0 / sample_rate_hz)
    fundamental_energy = _bin_amplitude(spectrum, freqs, f1_hz) ** 2
    fundamental_energy += _bin_amplitude(spectrum, freqs, f2_hz) ** 2

    distortion_energy = 0.0
    for m in range(-max_order, max_order + 1):
        for n in range(-max_order, max_order + 1):
            if abs(m) + abs(n) < 2 or abs(m) + abs(n) > max_order:
                continue
            freq = abs(m * f1_hz + n * f2_hz)
            if 0 < freq < sample_rate_hz / 2 and not np.isclose(freq, f1_hz) and not np.isclose(freq, f2_hz):
                distortion_energy += _bin_amplitude(spectrum, freqs, freq) ** 2
    return float(np.sqrt(distortion_energy) / max(np.sqrt(fundamental_energy), 1e-12))


def _paired(reference: np.ndarray, estimate: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    reference = np.asarray(reference, dtype=float)
    estimate = np.asarray(estimate, dtype=float)
    if reference.shape != estimate.shape:
        raise ValueError(f"Shape mismatch: {reference.shape} != {estimate.shape}")
    return reference, estimate


def _stft_mag(signal: np.ndarray, n_fft: int, hop_length: int) -> np.ndarray:
    if signal.size < n_fft:
        signal = np.pad(signal, (0, n_fft - signal.size))
    frames = []
    window = np.hanning(n_fft)
    for start in range(0, signal.size - n_fft + 1, hop_length):
        frames.append(np.abs(np.fft.rfft(signal[start : start + n_fft] * window)))
    return np.stack(frames) if frames else np.zeros((0, n_fft // 2 + 1))


def _bin_amplitude(spectrum: np.ndarray, freqs: np.ndarray, target_hz: float) -> float:
    return float(spectrum[int(np.argmin(np.abs(freqs - target_hz)))])
