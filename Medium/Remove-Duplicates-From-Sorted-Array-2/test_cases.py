"""A collection of test cases and solutions for `remove_duplicates_from_sorted_array_2.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `remove_duplicates_from_sorted_array_2.py` tests.
    """

    test_string = "Case: Example case."
    test_list = [1, 1, 1, 2, 2, 3]
    correct = [1, 1, 2, 2, 3, "X"]
    correct_k = 5
    test_1 = [test_list, correct, correct_k, test_string]

    test_string = "Case: Example case."
    test_list = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    correct = [0, 0, 1, 1, 2, 3, 3, "X", "X"]
    correct_k = 7
    test_2 = [test_list, correct, correct_k, test_string]

    test_string = "Case: Single Item."
    test_list = [0]
    correct = [0]
    correct_k = 1
    test_3 = [test_list, correct, correct_k, test_string]

    test_string = "Case: Two Items."
    test_list = [0, 0]
    correct = [0, 0]
    correct_k = 2
    test_4 = [test_list, correct, correct_k, test_string]

    test_string = "Case: Three Same Items."
    test_list = [0, 0, 0]
    correct = [0, 0, 0]
    correct_k = 2
    test_5 = [test_list, correct, correct_k, test_string]

    test_string = "Case: Three Different Items."
    test_list = [1, 3, 6]
    correct = [1, 3, 6]
    correct_k = 3
    test_6 = [test_list, correct, correct_k, test_string]

    test_string = "Case: Several of One Item."
    test_list = [-1, -1, -1, -1, -1, -1]
    correct = [-1, -1, "X", "X", "X", "X"]
    correct_k = 2
    test_7 = [test_list, correct, correct_k, test_string]

    test_string = "Case: Large Generated, Many of Two Items."
    test_list = []
    for _ in range(0, 1000):
        test_list.append(1)
    for _ in range(0, 800):
        test_list.append(2)
    correct = [1, 1, 2, 2, "X", "X", "X"]
    correct_k = 4
    test_8 = [test_list, correct, correct_k, test_string]
