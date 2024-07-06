"""A collection of test cases and solutions for `majority_element.py` tests."""

import random


class TestCases:
    """
    A collection of test cases and solutions for `majority_element.py` tests.
    """

    test_string = "Case: Example case."
    test_list = [3, 0, 6, 1, 5]
    correct = 3
    test_1 = [test_list, correct, test_string]

    test_string = "Case: Example case."
    test_list = [1, 3, 1]
    correct = 1
    test_2 = [test_list, correct, test_string]

    test_string = "Case: Single item, value equals count."
    test_list = [1]
    correct = 1
    test_3 = [test_list, correct, test_string]

    test_string = "Case: Two items, value equals count."
    test_list = [2, 2]
    correct = 2
    test_4 = [test_list, correct, test_string]

    test_string = "Case: Three items, citation number lower than count."
    test_list = [2, 2, 2]
    correct = 2
    test_5 = [test_list, correct, test_string]

    test_string = "Case: Three items, count lower than citations."
    test_list = [4, 4, 4]
    correct = 3
    test_6 = [test_list, correct, test_string]

    test_string = "Case: Larger list."
    test_list = [2, 4, 8, 3, 2, 6, 9, 9, 3, 1, 1, 1, 10, 11, 3]
    correct = 6
    test_7 = [test_list, correct, test_string]

    test_string = "Case: Single item, value larger than count."
    test_list = [9]
    correct = 1
    test_8 = [test_list, correct, test_string]

    test_string = "Case: Single item, zero citations."
    test_list = [0]
    correct = 0
    test_9 = [test_list, correct, test_string]

    test_string = "Case: Many zeros, then three 3s."
    test_list = []
    for i in range(0, 2000):
        test_list.append(0)
    test_list.append(3)
    test_list.append(3)
    test_list.append(3)
    correct = 3
    test_10 = [test_list, correct, test_string]
