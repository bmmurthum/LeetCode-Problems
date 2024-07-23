"""A collection of test cases and solutions for `rotate_image.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `rotate_image.py` tests.
    """

    test_string = "Case: Example case."
    test_input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    correct = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    test_1 = [test_input, correct, test_string]

    test_string = "Case: Example case 2."
    test_input = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    correct = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    test_2 = [test_input, correct, test_string]

    test_string = "Case: Width of 1."
    test_input = [[1]]
    correct = [[1]]
    test_3 = [test_input, correct, test_string]

    test_string = "Case: Width of 2."
    test_input = [[1, 2], [3, 4]]
    correct = [[3, 1], [4, 2]]
    test_4 = [test_input, correct, test_string]

    test_string = "Case: Width of 5."
    test_input = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    correct = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]
    test_5 = [test_input, correct, test_string]

    test_string = "Case: All same number."
    test_input = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    correct = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    test_6 = [test_input, correct, test_string]
