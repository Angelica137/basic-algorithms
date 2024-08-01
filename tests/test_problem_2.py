from src.problem_2 import rotated_array_search


def test_rotated_array_search_6():
    input = [6, 7, 8, 9, 10, 1, 2, 3, 4]
    n = 6
    assert rotated_array_search(input, n) == 6


def test_rotated_array_search_6():
    input = [6, 7, 8, 9, 10, 1, 2, 3, 4]
    n = 33
    assert rotated_array_search(input, n) == -1
