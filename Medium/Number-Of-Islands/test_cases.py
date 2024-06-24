"""A collection of test cases and solutions for `number_of_islands.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `number_of_islands.py` tests."""

    test_string = "Case: Checkerboard of islands."
    island_list = [
        ["1", "0", "1", "0", "1"],
        ["0", "1", "0", "1", "0"],
        ["1", "0", "1", "0", "1"],
        ["0", "1", "0", "1", "0"],
    ]
    correct = 10
    test_1 = [island_list, correct, test_string]

    test_string = "Case: Ring island, plus 1."
    island_list = [
        ["1", "1", "1", "0", "0"],
        ["1", "0", "1", "0", "0"],
        ["1", "1", "1", "0", "1"],
        ["0", "0", "0", "0", "0"],
    ]
    correct = 2
    test_2 = [island_list, correct, test_string]

    test_string = "Case: Single land."
    island_list = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "1"],
    ]
    correct = 1
    test_3 = [island_list, correct, test_string]

    test_string = "Case: Given example."
    island_list = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    correct = 1
    test_4 = [island_list, correct, test_string]

    test_string = "Case: Given example 2."
    island_list = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    correct = 3
    test_5 = [island_list, correct, test_string]

    test_string = "Case: All land."
    island_list = [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
    ]
    correct = 1
    test_6 = [island_list, correct, test_string]

    test_string = "Case: All water."
    island_list = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    correct = 0
    test_7 = [island_list, correct, test_string]

    test_string = "Case: One row."
    island_list = [["1", "0", "0", "1", "0"]]
    correct = 2
    test_8 = [island_list, correct, test_string]

    test_string = "Case: One column."
    island_list = [["1"], ["0"], ["1"], ["0"], ["0"]]
    correct = 2
    test_9 = [island_list, correct, test_string]

    test_string = "Case: Single item list, with land."
    island_list = [["1"]]
    correct = 1
    test_10 = [island_list, correct, test_string]

    test_string = "Case: Single item list, with water."
    island_list = [["0"]]
    correct = 0
    test_11 = [island_list, correct, test_string]
