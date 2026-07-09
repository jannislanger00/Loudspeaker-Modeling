from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class VerificationResult:
    input_path: str
    output_path: str
    sample_rate: int
    delay_samples: int
    input_rms_db: float
    output_rms_db: float
    clipped_input: bool
    clipped_output: bool
    freqs: np.ndarray
    frequency_response_db: np.ndarray
    residual: np.ndarray

    @property
    def summary(self) -> dict:
        return {
            "input_path": self.input_path,
            "output_path": self.output_path,
            "sample_rate": self.sample_rate,
            "delay_samples": self.delay_samples,
            "input_rms_db": round(self.input_rms_db, 2),
            "output_rms_db": round(self.output_rms_db, 2),
            "clipped_input": self.clipped_input,
            "clipped_output": self.clipped_output,
        }

    def plot_frequency_response(self):
        plt.figure(figsize=(8, 4))
        plt.semilogx(self.freqs, self.frequency_response_db)
        plt.xlabel("Frequency [Hz]")
        plt.ylabel("Magnitude [dB]")
        plt.title("Estimated Frequency Response")
        plt.grid(True, which="both")
        plt.show()

    def plot_residual(self, n_samples=3000):
        plt.figure(figsize=(8, 4))
        plt.plot(self.residual[:n_samples])
        plt.xlabel("Samples")
        plt.ylabel("Amplitude")
        plt.title("Model Residual")
        plt.grid(True)
        plt.show()


