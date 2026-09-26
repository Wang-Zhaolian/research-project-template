# Data Policy

Do not commit confidential data, licensed datasets, or large generated files.

- Put small redistributable examples in `data/sample/` when useful.
- Keep raw, interim, and processed bulk data outside Git.
- Record source, license, version, retrieval date, and checksum here.
- Use machine-local paths or environment variables instead of hard-coded
  absolute paths.

If `raw/`, `interim/`, or `processed/` directories are created, their bulk
contents are ignored by the repository rules.
