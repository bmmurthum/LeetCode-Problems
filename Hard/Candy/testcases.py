"""A collection of test cases and solutions for `candy.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `candy.py` tests.
    """

    test_string = "Case 1: Example 1."
    test_input_1 = [1, 0, 2]
    correct = 5
    test_1 = [test_input_1, correct, test_string]

    test_string = "Case 2: Example 2."
    test_input_1 = [1, 2, 2]
    correct = 4
    test_2 = [test_input_1, correct, test_string]

    test_string = "Case 3: All equal rated children."
    test_input_1 = [1, 1, 1, 1]
    correct = 4
    test_3 = [test_input_1, correct, test_string]

    test_string = "Case 4: Ascending."
    test_input_1 = [1, 2, 3, 4, 5, 6, 7]
    correct = 28
    test_4 = [test_input_1, correct, test_string]

    test_string = "Case 5: Descending."
    test_input_1 = [7, 6, 5, 4, 3, 2, 1]
    correct = 28
    test_5 = [test_input_1, correct, test_string]

    test_string = "Case 6: Lowest in middle."
    test_input_1 = [7, 6, 5, 4, 5, 6, 7]
    correct = 19
    test_6 = [test_input_1, correct, test_string]

    test_string = "Case 7: Highest in middle."
    test_input_1 = [1, 2, 3, 4, 3, 2, 1]
    correct = 16
    test_7 = [test_input_1, correct, test_string]

    test_string = "Case 7b: Highest in middle alternate."
    test_input_1 = [1, 2, 3, 4, 2, 1, 0]
    correct = 16
    test_7b = [test_input_1, correct, test_string]

    test_string = "Case 7c: Highest in middle alternate."
    test_input_1 = [1, 2, 3, 4, 4, 3, 2, 1]
    correct = 20
    test_7c = [test_input_1, correct, test_string]

    test_string = "Case 8: Alternating high and low."
    test_input_1 = [1, 5, 1, 3, 1, 6, 2]
    correct = 10
    test_8 = [test_input_1, correct, test_string]

    test_string = "Case 9: Alternating high and low."
    test_input_1 = [0, 9, 8, 9, 7, 9, 0]
    correct = 10
    test_9 = [test_input_1, correct, test_string]

    test_string = "Case 10: 1000-long. Alternating high and low."
    test_input_1 = []
    for _ in range(1000):
        test_input_1.append(0)
        test_input_1.append(1)
    correct = 3000
    test_10 = [test_input_1, correct, test_string]

    test_string = "Case 11: 1000-long. All equal ratings."
    test_input_1 = []
    for _ in range(1000):
        test_input_1.append(1)
    correct = 1000
    test_11 = [test_input_1, correct, test_string]

    test_string = "Case 12: 1000-long. Ascending."
    test_input_1 = []
    for i in range(1, 1000):
        test_input_1.append(i)
    correct = 499500
    test_12 = [test_input_1, correct, test_string]

    test_string = "Case 13: Mixed case."
    test_input_1 = [
        4,
        3,
        4,
        5,
        5,
        5,
        5,
        4,
        3,
        2,
        1,
        2,
        1,
        2,
        1,
        1,
        1,
        1,
        2,
        2,
        3,
        2,
        2,
        4,
    ]
    correct = 43
    test_13 = [test_input_1, correct, test_string]

    test_string = "Case 14: More plateaus."
    test_input_1 = [0, 0, 1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 3, 4, 4, 5, 6, 6, 5, 5, 6, 7, 7]
    correct = 37
    test_14 = [test_input_1, correct, test_string]

    test_string = "Case 15: Replacing old candy records."
    test_input_1 = [3, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 2, 3, 3, 3]
    correct = 34
    test_15 = [test_input_1, correct, test_string]

    test_string = "Case 16: Single child."
    test_input_1 = [1]
    correct = 1
    test_16 = [test_input_1, correct, test_string]

    test_string = "Case 17: Two equal children."
    test_input_1 = [2, 2]
    correct = 2
    test_17 = [test_input_1, correct, test_string]

    test_string = "Case 18: Two unequal children."
    test_input_1 = [1, 2]
    correct = 3
    test_18 = [test_input_1, correct, test_string]
