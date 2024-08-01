"""A collection of test cases and solutions for `jump_game_ii.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `jump_game_ii.py` tests.
    """

    test_string = "Case: Example 1."
    test_input = [2, 3, 1, 1, 4]
    correct = 2
    test_1 = [test_input, correct, test_string]

    test_string = "Case: Example 2."
    test_input = [2, 3, 0, 1, 4]
    correct = 2
    test_2 = [test_input, correct, test_string]

    test_string = "Case: All ones."
    test_input = [1, 1, 1, 1, 1, 1]
    correct = 5
    test_3 = [test_input, correct, test_string]

    test_string = "Case: Jumping a gap."
    test_input = [10, 0, 0, 5, 0, 0, 0, 0]
    correct = 1
    test_4 = [test_input, correct, test_string]

    test_string = "Case: All tens."
    test_input = [10, 10, 10, 10, 10, 10, 10, 10]
    correct = 1
    test_5 = [test_input, correct, test_string]

    test_string = "Case: Single item."
    test_input = [1]
    correct = 0
    test_6 = [test_input, correct, test_string]

    test_string = "Case: 1000 ones."
    test_input = []
    for i in range(1000):
        test_input.append(1)
    correct = 999
    test_7 = [test_input, correct, test_string]

    test_string = "Case: 1000 ones. Jumpable."
    test_input = [1000]
    for i in range(999):
        test_input.append(1)
    correct = 1
    test_8 = [test_input, correct, test_string]
