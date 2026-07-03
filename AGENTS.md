# Agent Instructions

You are assisting with a scientific coding project.

## Rules

1. Do not make scientific, statistical, or methodological decisions without asking.
2. Do not change preprocessing, exclusion criteria, model choice, or evaluation metrics unless explicitly instructed.
3. Work in small steps.
4. Before editing, state which files you will change and why.
5. After editing, summarize the diff, assumptions, tests run, and remaining risks.
6. Prefer adding tests over adding features.
7. Preserve reproducibility: fixed seeds, environment files, exact data versions, and deterministic outputs where possible.
8. If uncertain, stop and ask rather than guessing.

## Project Shape

- Keep the repository minimal until the scientific workflow requires more.
- `scripts/` contains command-line entrypoints.
- `src/loudspeaker_modeling/` contains reusable code.
- `tests/` contains safety checks for implemented behavior.
- `params.yaml` contains explicit parameters chosen by the researcher.
