from src.problem_4 import sort_012


def test_sort_012_returns_0():
    assert sort_012([0]) == [0]


def test_sort_012_returns_012():
    assert sort_012([0, 2, 1]) == [0, 1, 2]


def test_sort_012_returns_002():
    assert sort_012([2, 0, 0]) == [0, 0, 2]