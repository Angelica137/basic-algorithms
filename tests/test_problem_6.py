from src.problem_6 import get_min_max


def test_get_min_max_returns_0_2():
    ints = [1, 0, 2, 1]
    assert get_min_max(ints) == (0, 2)


def test_get_min_max_returns_None():
    ints = []
    assert get_min_max(ints) is None
