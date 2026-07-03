# Expose Summary

Working title: Neural grey-box modeling and compensation of nonlinear
loudspeaker distortion.

## Research Questions

- RQ1: How well do residual grey-box models predict nonlinear dynamic
  distortion compared with classical block-oriented and black-box approaches?
- RQ2: How well do the models generalize across input levels, frequency ranges,
  and signal types when trained and evaluated on real microphone measurements?
- RQ3: Can a sufficiently accurate forward model be used for model-based
  predistortion that reduces measured harmonic and intermodulation distortion?

## Planned Model Classes

- Linear FIR/IIR reference model.
- Parallel Hammerstein model as a structured nonlinear baseline.
- Black-box TCN forward model.
- Residual grey-box model over the linear baseline.
- Residual grey-box model over the Hammerstein baseline.
- Direct inverse and model-based end-to-end predistortion if the forward-model
  quality is sufficient.

## Evaluation

Primary evaluation levels:

- Forward-model quality: MSE, ESR, STFT error, THD prediction, IMD prediction.
- System-level compensation: measured THD/IMD reduction at the physical
  loudspeaker output.

## Schedule

The planned thesis period is 2026-07-01 to 2026-10-31, organized in two-week
work packages from measurement planning through data capture, baselines, neural
models, grey-box models, systematic evaluation, compensation tests, and writing.
