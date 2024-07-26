"""A collection of test cases and solutions for `insert_interval.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `insert_interval.py` tests.
    """

    test_string = "Case: Example 1."
    test_input_1 = [[1, 3], [6, 9]]
    test_input_2 = [2, 5]
    correct = [[1, 5], [6, 9]]
    test_1 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Example 2."
    test_input_1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    test_input_2 = [4, 8]
    correct = [[1, 2], [3, 10], [12, 16]]
    test_2 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Intervals can be one value wide."
    test_input_1 = [[1, 1], [2, 2]]
    test_input_2 = [2, 5]
    correct = [[1, 1], [2, 5]]
    test_3 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: One item in intervals."
    test_input_1 = [[0, 0]]
    test_input_2 = [0, 3]
    correct = [[0, 3]]
    test_4 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: One item in intervals 2."
    test_input_1 = [[0, 0]]
    test_input_2 = [2, 3]
    correct = [[0, 0], [2, 3]]
    test_5 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: No items in intervals."
    test_input_1 = []
    test_input_2 = [2, 3]
    correct = [[2, 3]]
    test_6 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Many items now one."
    test_input_1 = [[1, 2], [3, 3], [4, 4], [5, 5], [6, 7]]
    test_input_2 = [1, 7]
    correct = [[1, 7]]
    test_7 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: New interval in beginning."
    test_input_1 = [[3, 4], [5, 5], [6, 7], [8, 10]]
    test_input_2 = [1, 2]
    correct = [[1, 2], [3, 4], [5, 5], [6, 7], [8, 10]]
    test_8 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: New interval at end."
    test_input_1 = [[3, 4], [5, 5], [6, 7], [8, 10]]
    test_input_2 = [12, 13]
    correct = [[3, 4], [5, 5], [6, 7], [8, 10], [12, 13]]
    test_9 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: New interval completely inside the original."
    test_input_1 = [[1, 10]]
    test_input_2 = [2, 5]
    correct = [[1, 10]]
    test_10 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Original item completely inside the new interval."
    test_input_1 = [[4, 5]]
    test_input_2 = [2, 7]
    correct = [[2, 7]]
    test_11 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: New interval completely inside another."
    test_input_1 = [[1, 10], [11, 12], [13, 15]]
    test_input_2 = [2, 5]
    correct = [[1, 10], [11, 12], [13, 15]]
    test_12 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: New interval near beginning."
    test_input_1 = [[5, 10], [11, 12], [13, 15]]
    test_input_2 = [1, 6]
    correct = [[1, 10], [11, 12], [13, 15]]
    test_13 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: New interval overlaps all intervals."
    test_input_1 = [[1, 5], [6, 8]]
    test_input_2 = [0, 9]
    correct = [[0, 9]]
    test_14 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: New interval never overlaps, within group."
    test_input_1 = [[1, 1], [2, 3], [7, 7], [8, 8], [9, 10], [11, 11]]
    test_input_2 = [5, 6]
    correct = [[1, 1], [2, 3], [5, 6], [7, 7], [8, 8], [9, 10], [11, 11]]
    test_15 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: New interval overlaps some intervals."
    test_input_1 = [[0, 0], [2, 4], [9, 9]]
    test_input_2 = [0, 7]
    correct = [[0, 7], [9, 9]]
    test_16 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: New interval overlaps some intervals 2."
    test_input_1 = [[0, 0], [2, 4], [9, 9]]
    test_input_2 = [1, 9]
    correct = [[0, 0], [1, 9]]
    test_17 = [test_input_1, test_input_2, correct, test_string]
