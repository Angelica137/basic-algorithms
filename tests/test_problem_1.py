import pytest
from src.problem_1 import sqrt


def test_sqrt_0_is_0():
    assert sqrt(0) == 0


def test_sqrt_1_is_1():
    assert sqrt(1) == 1


def test_sqrt_negative_returns_error():
    with pytest.raises(ValueError, match="Cannot compute square root of negative number"):
        sqrt(-1)


def test_sqrt_9_is_3():
    assert sqrt(9) == 3


def test_sqrt_27_is_5():
    assert sqrt(27) == 5
