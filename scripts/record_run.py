"""Create a small experiment record linked to the current Git commit."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path


EXPERIMENT_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def current_commit() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment-id", required=True)
    parser.add_argument("--config", type=Path, required=True)
    args = parser.parse_args()

    if not EXPERIMENT_ID.fullmatch(args.experiment_id):
        parser.error("experiment ID may contain letters, digits, dot, dash, underscore")
    if not args.config.is_file():
        parser.error(f"config does not exist: {args.config}")

    record = {
        "experiment_id": args.experiment_id,
        "commit": current_commit(),
        "config": args.config.as_posix(),
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
    }

    output_dir = Path("results") / "runs" / args.experiment_id
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / "metadata.json"
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
