# Agent Instructions

This repository is a master thesis workspace. The researcher must stay informed
and in control of scientific and structural decisions.

## Current Phase

The project is currently in Phase 1: measurement planning, raw-data
organization, preprocessing, and basic metrics.

Do not add model training, grey-box modeling, thesis writing scaffolds, or
compensation code unless the user explicitly asks to move into that phase.

## Decision Rules

- Explain what you are changing and why before making structural changes.
- Keep `params.yaml` as the only active configuration source.
- Put scientific parameters in `params.yaml`.
- Put the reason for non-obvious choices in `docs/decisions.md`.
- Put executed experiments and observations in `docs/experiment_log.md`.
- If a change creates a new workflow, add a short explanation to `README.md`.
- Separate implemented behavior from future plans. Do not create placeholder
  files for future phases unless they directly help the current phase.

## Data Rules

- Never modify raw measurement files under `data/raw/`.
- `data/raw/manifest.csv` is the index of raw recordings and may be edited.
- Derived files belong in `data/interim/` or `data/processed/`.
- Large data and generated artifacts should be handled with DVC, not committed
  directly to Git.

## Code Rules

- Scripts in `scripts/` are terminal entrypoints.
- Reusable logic belongs in `src/loudspeaker_modeling/`.
- Tests belong in `tests/`.
- Prefer small, transparent functions over large abstract frameworks.
- Do not introduce a new dependency without explaining why it is needed.

## Acceptance Checks

Run these before handing off meaningful changes:

```powershell
python -m pytest
python scripts/preprocess_dataset.py --params params.yaml
python scripts/evaluate_model.py --params params.yaml
```

When DVC is initialized and data exists, also run:

```powershell
dvc repro evaluate
```
