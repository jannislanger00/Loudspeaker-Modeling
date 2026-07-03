# Loudspeaker Modeling

Reproducible research workspace for a master thesis on neural grey-box modeling
and compensation of nonlinear loudspeaker distortion.

The repository is currently kept intentionally small. It is in the starting
phase: measurement planning, raw-data organization, preprocessing, and basic
evaluation metrics.

The full thesis will eventually follow this pipeline:

1. Record synchronized electrical input and acoustic/mechanical outputs.
2. Preprocess raw measurements into aligned, segmented datasets.
3. Characterize the measured loudspeaker with basic metrics and plots.
4. Train forward models: linear FIR/IIR, parallel Hammerstein, black-box TCN,
   and residual grey-box variants.
5. Evaluate time-domain error, spectral error, THD, IMD, generalization,
   stability, and compute cost.
6. Attempt predistortion only after a forward-model accuracy gate is met.

Only the first parts are implemented now. Later phases should be added only
when the scientific work reaches them.

## Setup

Recommended environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .[dev]
```

If you use `uv`, the equivalent is:

```powershell
uv venv
uv pip install -e .[dev]
```

## DVC Setup

Large measurement data and generated artifacts should not be committed directly
to Git. Initialize DVC and add a local remote, for example:

```powershell
python -m pip install -e .[data]
dvc init
dvc remote add -d local_remote C:\tmp\loudspeaker-modeling-dvc
dvc add data/raw data/processed artifacts/metrics
```

Commit the resulting `.dvc` metadata files, not the large binary data.

## How This Project Is Organized

The active source of truth for experiment decisions is `params.yaml`.

- `params.yaml`: scientific parameters, such as sample rate, model settings,
  splits, and evaluation settings.
- `scripts/`: commands you run from the terminal.
- `src/loudspeaker_modeling/`: reusable implementation used by the scripts.
- `docs/decisions.md`: why a decision was made.
- `docs/experiment_log.md`: what was run and what happened.
- `data/raw/manifest.csv`: index of raw measurements.
- `artifacts/`: generated models, metrics, and figures.

The working rule is:

```text
Decision -> params.yaml
Reason -> docs/decisions.md
Execution -> scripts/
Implementation -> src/
Result -> artifacts/
Interpretation -> docs/experiment_log.md or thesis/
```

## Common Commands

```powershell
python -m pytest
python scripts/preprocess_dataset.py --params params.yaml
python scripts/evaluate_model.py --params params.yaml
dvc repro evaluate
```

## Data Layout

Raw recordings are immutable. Put one row per recording in
`data/raw/manifest.csv` and store raw audio or measurement files under
`data/raw/recordings/`.

Processed data belongs under `data/interim/` or `data/processed/`. Generated
metrics belong under `artifacts/metrics/`.

## Current Milestone

Milestone 1 is measurement and data grounding: documentation, configuration,
manifest validation, preprocessing helpers, metric functions, and tests.
