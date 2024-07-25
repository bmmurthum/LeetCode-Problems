"""A collection of test cases and solutions for `longest_consecutive_sequence.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `longest_consecutive_sequence.py` tests.
    """

    test_string = "Case: Example 1."
    test_input = [100, 4, 200, 1, 3, 2]
    correct = 4
    test_1 = [test_input, correct, test_string]

    test_string = "Case: Example 2."
    test_input = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    correct = 9
    test_2 = [test_input, correct, test_string]

    test_string = "Case: Empty list."
    test_input = []
    correct = 0
    test_3 = [test_input, correct, test_string]

    test_string = "Case: Simple."
    test_input = [1, 2, 0, 1]
    correct = 3
    test_4 = [test_input, correct, test_string]

    test_string = "Case: One number."
    test_input = [0]
    correct = 1
    test_5 = [test_input, correct, test_string]

    test_string = "Case: Two same numbers."
    test_input = [0, 0]
    correct = 1
    test_6 = [test_input, correct, test_string]

    test_string = "Case: Two different numbers."
    test_input = [1, 2]
    correct = 2
    test_7 = [test_input, correct, test_string]

    test_string = "Case: 20-long chain. 30 total values."
    test_input = [
        -29,
        -494,
        40,
        1,
        2,
        8,
        7,
        6,
        3,
        4,
        9,
        14,
        15,
        11,
        10,
        12,
        19,
        13,
        5,
        16,
        17,
        18,
        20,
        2,
        16,
        266,
        200,
        438,
    ]
    correct = 20
    test_8 = [test_input, correct, test_string]
