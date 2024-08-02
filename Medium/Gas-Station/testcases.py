"""A collection of test cases and solutions for `gas_station.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `gas_station.py` tests.
    """

    test_string = "Case 1: Example 1."
    test_input_1 = [1, 2, 3, 4, 5]
    test_input_2 = [3, 4, 5, 1, 2]
    correct = 3
    test_1 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case 2: Example 2."
    test_input_1 = [2, 3, 4]
    test_input_2 = [3, 4, 3]
    correct = -1
    test_2 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case 3: Lots of gas at last index."
    test_input_1 = [1, 2, 3, 2, 0, 0, 8]
    test_input_2 = [3, 4, 5, 1, 1, 1, 1]
    correct = 6
    test_3 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case 4: Front loaded."
    test_input_1 = [2, 2, 2, 0, 0, 0]
    test_input_2 = [1, 1, 1, 1, 1, 1]
    correct = 0
    test_4 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case 5: Back loaded."
    test_input_1 = [0, 0, 0, 2, 2, 2]
    test_input_2 = [1, 1, 1, 1, 1, 1]
    correct = 3
    test_5 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case 6: General case."
    test_input_1 = [0, 2, 2, 0, 2, 0]
    test_input_2 = [1, 1, 1, 1, 1, 1]
    correct = 1
    test_6 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case 7: Starts at last index."
    test_input_1 = [2, 2, 0, 0, 0, 2]
    test_input_2 = [1, 1, 1, 1, 1, 1]
    correct = 5
    test_7 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case 8: 1000 Long. Front loaded."
    test_input_1 = []
    for i in range(500):
        test_input_1.append(2)
    for i in range(500):
        test_input_1.append(0)
    test_input_2 = [1] * 1000
    correct = 0
    test_8 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case 9: 1000 Long. Back loaded."
    test_input_1 = []
    for i in range(500):
        test_input_1.append(0)
    for i in range(500):
        test_input_1.append(2)
    test_input_2 = [1] * 1000
    correct = 500
    test_9 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case 10: 1000 Long. Starts at back index."
    test_input_1 = []
    for i in range(499):
        test_input_1.append(2)
    for i in range(500):
        test_input_1.append(0)
    test_input_1.append(2)
    test_input_2 = [1] * 1000
    correct = 999
    test_10 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case 11: 1000 Long. No valid start."
    test_input_1 = []
    for i in range(500):
        test_input_1.append(2)
        test_input_1.append(0)
    for i in range(10):
        test_input_1.append(0)
    for i in range(500):
        test_input_1.append(2)
        test_input_1.append(0)
    test_input_2 = [1] * 2010
    correct = -1
    test_11 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case 12: Single gas station."
    test_input_1 = [2]
    test_input_2 = [1]
    correct = 0
    test_12 = [test_input_1, test_input_2, correct, test_string]
