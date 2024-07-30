"""A collection of test cases and solutions for `best_time_to_buy_and_sell_stock.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `best_time_to_buy_and_sell_stock.py` tests.
    """

    test_string = "Case: Example 1."
    test_input = [7, 1, 5, 3, 6, 4]
    correct = 5
    test_1 = [test_input, correct, test_string]

    test_string = "Case: Example 2. All descending numbers."
    test_input = [7, 6, 4, 3, 1]
    correct = 0
    test_2 = [test_input, correct, test_string]

    test_string = "Case: All ascending numbers."
    test_input = [1, 2, 3, 4, 5, 6, 8, 12]
    correct = 11
    test_3 = [test_input, correct, test_string]

    test_string = "Case: Good beginning match, then another."
    test_input = [2, 9, 1, 9, 4, 3, 1]
    correct = 8
    test_4 = [test_input, correct, test_string]

    test_string = "Case: Same match in beginning and end."
    test_input = [0, 10, 1, 2, 3, 4, 2, 3, 6, 7, 2, 3, 6, 8, 0, 10]
    correct = 10
    test_5 = [test_input, correct, test_string]

    test_string = "Case: Minimum value at end."
    test_input = [3, 10, 2, 4, 5, 10, 0]
    correct = 8
    test_6 = [test_input, correct, test_string]

    test_string = "Case: Values all zero."
    test_input = [0, 0, 0, 0, 0, 0]
    correct = 0
    test_7 = [test_input, correct, test_string]

    test_string = "Case: List length of 1, minimum."
    test_input = [3]
    correct = 0
    test_8 = [test_input, correct, test_string]

    test_string = "Case: 1000 items, best sell at end."
    test_input = [0]
    for _ in range(1000):
        test_input.append(2)
    test_input.append(10)
    correct = 10
    test_9 = [test_input, correct, test_string]

    test_string = "Case: 1000 items, best sell near beginning."
    test_input = [0]
    test_input.append(10)
    for _ in range(1000):
        test_input.append(2)
    correct = 10
    test_10 = [test_input, correct, test_string]
