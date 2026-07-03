# Decisions

Record decisions that future agents or thesis-writing sessions need to respect.

## Accepted

### 2026-07-02 - Primary Implementation Stack

Use Python/PyTorch for preprocessing, models, training, and evaluation.

### 2026-07-02 - Data Versioning

Use DVC with a local remote for large measurement data and generated artifacts.

### 2026-07-02 - Thesis Writing

Keep LaTeX source in the repository so generated figures and written analysis
can stay reproducible.

### 2026-07-02 - Single Active Configuration File

Use `params.yaml` as the only active configuration source at the project start.
Separate files under `configs/` were removed to avoid duplicate places for
scientific decisions.

### 2026-07-02 - Phase-Based Repository Growth

Keep only the structure needed for the current research phase. Model training,
grey-box modeling, thesis writing scaffolds, and compensation code will be added
later when the thesis reaches those phases.

## Open

- Exact audio interface and channel mapping.
- Exact loudspeaker IDs.
- Final measurement levels after safety checks.
- Compensation accuracy gate after the first model evaluation.
