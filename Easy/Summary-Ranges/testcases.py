"""A collection of test cases and solutions for `summary_ranges.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `summary_ranges.py` tests.
    """

    test_string = "Case: Example 1."
    test_input = [0, 1, 2, 4, 5, 7]
    correct = ["0->2", "4->5", "7"]
    test_1 = [test_input, correct, test_string]

    test_string = "Case: Example 2."
    test_input = [0, 2, 3, 4, 6, 8, 9]
    correct = ["0", "2->4", "6", "8->9"]
    test_2 = [test_input, correct, test_string]

    test_string = "Case: Some negative values and zero."
    test_input = [-10, -9, 0, 1, 2, 3, 4, 7, 8, 9]
    correct = ["-10->-9", "0->4", "7->9"]
    test_3 = [test_input, correct, test_string]

    test_string = "Case: Empty list."
    test_input = []
    correct = []
    test_4 = [test_input, correct, test_string]

    test_string = "Case: Single item."
    test_input = [2]
    correct = ["2"]
    test_5 = [test_input, correct, test_string]

    test_string = "Case: 20 items, not touching."
    test_input = [
        1,
        3,
        5,
        7,
        9,
        11,
        13,
        15,
        17,
        19,
        22,
        24,
        26,
        28,
        30,
        32,
        34,
        36,
        38,
        40,
    ]
    correct = [
        "1",
        "3",
        "5",
        "7",
        "9",
        "11",
        "13",
        "15",
        "17",
        "19",
        "22",
        "24",
        "26",
        "28",
        "30",
        "32",
        "34",
        "36",
        "38",
        "40",
    ]
    test_6 = [test_input, correct, test_string]

    test_string = "Case: 20 items, all together."
    test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    correct = ["1->20"]
    test_7 = [test_input, correct, test_string]
