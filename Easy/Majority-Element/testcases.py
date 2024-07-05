"""A collection of test cases and solutions for `majority_element.py` tests."""

import random


class TestCases:
    """
    A collection of test cases and solutions for `majority_element.py` tests.
    """

    test_string = "Case: Example case."
    test_list = [2, 2, 1, 1, 1, 2, 2]
    correct = 2
    test_1 = [test_list, correct, test_string]

    test_string = "Case: Example case."
    test_list = [3, 2, 3]
    correct = 3
    test_2 = [test_list, correct, test_string]

    # Removed tests for no-answer. Other answers do not account for
    # impossibility.

    # test_string = "Case: None, even case."
    # test_list = [1, 1, 2, 2]
    # correct = None
    # test_3 = [test_list, correct, test_string]

    # test_string = "Case: None, even case."
    # test_list = [1, 3]
    # correct = None
    # test_4 = [test_list, correct, test_string]

    test_string = "Case: Two items."
    test_list = [1, 1]
    correct = 1
    test_5 = [test_list, correct, test_string]

    test_string = "Case: One item."
    test_list = [3]
    correct = 3
    test_6 = [test_list, correct, test_string]

    test_string = "Case: Larger 5000-item generated list."
    item_list = [1, 2, 5]
    test_list = random.choices(item_list, weights=[3, 1, 1], k=5000)
    correct = 1
    test_7 = [test_list, correct, test_string]
