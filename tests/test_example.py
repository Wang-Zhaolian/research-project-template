from research_project.example import mean_center


def test_mean_center() -> None:
    assert mean_center([1.0, 2.0, 3.0]) == [-1.0, 0.0, 1.0]


def test_mean_center_empty() -> None:
    assert mean_center([]) == []
