"""A collection of test cases and solutions for `jump_game.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `jump_game.py` tests.
    """

    test_string = "Case: Example 1."
    test_input = [2, 3, 1, 1, 4]
    correct = True
    test_1 = [test_input, correct, test_string]

    test_string = "Case: Example 2."
    test_input = [3, 2, 1, 0, 4]
    correct = False
    test_2 = [test_input, correct, test_string]

    test_string = "Case: Many ones. Zero as last number."
    test_input = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    correct = True
    test_3 = [test_input, correct, test_string]

    test_string = "Case: Quick jump to end."
    test_input = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    correct = True
    test_4 = [test_input, correct, test_string]

    test_string = "Case: Single item."
    test_input = [2]
    correct = True
    test_5 = [test_input, correct, test_string]

    test_string = "Case: Jump several zeroes to end."
    test_input = [3, 0, 0, 2, 0, 2, 0, 2, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0]
    correct = True
    test_6 = [test_input, correct, test_string]

    test_string = "Case: Zero at beginning."
    test_input = [0, 1, 2, 1]
    correct = False
    test_7 = [test_input, correct, test_string]

    test_string = "Case: Zero at beginning 2."
    test_input = [0, 1, 2, 1]
    correct = False
    test_8 = [test_input, correct, test_string]

    test_string = "Case: Zero at beginning. Single item."
    test_input = [0]
    correct = True
    test_9 = [test_input, correct, test_string]
