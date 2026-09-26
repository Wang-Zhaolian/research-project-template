# Research Project

Private-by-default template for reproducible computational research.

## Project

Replace this section with the research question, scope, and intended users.

## Motivation

Explain why the question matters and what gap the project addresses.

## Status

`Planning` — update this to `Active`, `Paused`, `Completed`, or `Archived`.

## Setup

Requires Python 3.11 or newer.

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Activate `.venv` using the command appropriate for the current operating
system. Never commit the environment directory itself.

## Usage

```bash
python -m research_project.example
pytest
```

## Structure

- `configs/`: versioned experiment configuration.
- `data/`: data policy and small, redistributable samples only.
- `docs/`: decisions, protocols, and reproducibility notes.
- `experiments/`: experiment index and hypotheses.
- `notebooks/`: exploration; reusable logic belongs in `src/`.
- `scripts/`: reproducible entry points and utility commands.
- `src/`: reusable source code.
- `tests/`: automated checks.
- `results/`: small metrics and summaries linked to commits.
- `reports/`: manuscripts, figures, and presentation source files.

## Experiments

Every important run should record at least:

- an experiment ID;
- the Git commit hash;
- a versioned config path;
- dataset identity or checksum;
- environment information;
- metrics and a short conclusion.

Example: `E023` at commit `abc1234` using
`configs/baseline.yaml`.

## Results

Track compact tables, figures, and conclusions. Keep datasets, checkpoints,
caches, and large raw logs outside normal Git history.

## Notes

This repository starts private. Review data licenses, third-party licenses,
secrets, authorship, and documentation before any decision to make it public.
