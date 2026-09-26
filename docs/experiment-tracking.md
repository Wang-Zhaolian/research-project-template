# Experiment Tracking

Git versions code; it is not an experiment database.

For every important run, record:

| Field | Example |
|---|---|
| Experiment ID | `E023` |
| Commit | `abc1234` |
| Config | `configs/baseline.yaml` |
| Dataset | name, version, checksum |
| Environment | Python and dependency versions |
| Metrics | compact machine-readable summary |
| Conclusion | what was learned and what comes next |

Run `python scripts/record_run.py --experiment-id E023 --config
configs/baseline.yaml` before or immediately after the experiment to create a
small metadata record under `results/runs/`.
