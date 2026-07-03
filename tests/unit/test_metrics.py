import numpy as np

from loudspeaker_modeling.evaluation.metrics import esr, mse, thd


def test_mse_zero_for_identical_signals():
    signal = np.array([1.0, 2.0, 3.0])
    assert mse(signal, signal) == 0.0


def test_esr_zero_for_identical_signals():
    signal = np.array([1.0, 2.0, 3.0])
    assert esr(signal, signal) == 0.0


def test_thd_is_small_for_pure_sine():
    sample_rate = 48000
    t = np.arange(sample_rate) / sample_rate
    signal = np.sin(2 * np.pi * 1000 * t)
    assert thd(signal, sample_rate, 1000, max_harmonic=5) < 1e-10
