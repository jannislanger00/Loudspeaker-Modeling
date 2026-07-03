# Loudspeaker Modeling

Minimum reproducible scientific loop for a master thesis on loudspeaker
modeling.

The repository is deliberately small. It should grow only when the scientific
workflow needs the next piece.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .[dev]
```

## Project Structure

```text
data/
  raw/
  processed/
docs/
  experiment_log.md
  decisions.md
notebooks/
scripts/
  preprocess_dataset.py
  train_model.py
  evaluate_model.py
src/loudspeaker_modeling/
  preprocessing.py
  features.py
  model.py
  metrics.py
tests/
  test_preprocessing.py
```

## Common Commands

```powershell
python -m pytest
python scripts/preprocess_dataset.py --params params.yaml
python scripts/train_model.py --params params.yaml
python scripts/evaluate_model.py --params params.yaml
```

## Data Layout

Raw recordings belong in `data/raw/`. Derived files belong in
`data/processed/`.

Raw data should be treated as immutable. If a raw recording is flawed, keep it
unchanged and document the issue instead of editing the file.

## Current Milestone

Milestone 1 is to establish the smallest reproducible loop:

1. Put raw data in `data/raw/`.
2. Run one explicit preprocessing step.
3. Train one explicitly chosen model.
4. Evaluate with explicitly chosen metrics.
5. Record what happened in `docs/experiment_log.md`.
