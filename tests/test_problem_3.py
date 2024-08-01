from src.problem_3 import rearrange_digits


def test_rearrange_digits_531_42():
    input_list = [1, 2, 3, 4, 5]
    assert rearrange_digits(input_list) == [531, 42]


def test_rearrange_digits_531_42():
    input_list = [4, 6, 2, 5, 9, 8]
    assert rearrange_digits(input_list) == [964, 852]
