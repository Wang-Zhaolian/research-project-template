"""Small deterministic example used by the template smoke test."""

from __future__ import annotations


def mean_center(values: list[float]) -> list[float]:
    """Return values centered around their arithmetic mean."""
    if not values:
        return []
    mean = sum(values) / len(values)
    return [value - mean for value in values]


if __name__ == "__main__":
    print(mean_center([1.0, 2.0, 3.0]))
