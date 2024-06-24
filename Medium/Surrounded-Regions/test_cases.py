"""A collection of test cases and solutions for `surrounded_regions.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `surrounded_regions.py` tests."""

    test_string = "Case: Example case."
    region_list = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    correct = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    test_1 = [region_list, correct, test_string]

    test_string = "Case: Single item with X."
    region_list = [["X"]]
    correct = [["X"]]
    test_2 = [region_list, correct, test_string]

    test_string = "Case: Single item with O."
    region_list = [["O"]]
    correct = [["O"]]
    test_3 = [region_list, correct, test_string]

    test_string = "Case: No possible surrounds 1."
    region_list = [["X", "X", "X", "X", "X", "X"], ["X", "O", "O", "O", "X", "X"]]
    correct = [["X", "X", "X", "X", "X", "X"], ["X", "O", "O", "O", "X", "X"]]
    test_4 = [region_list, correct, test_string]

    test_string = "Case: No possible surrounds 2."
    region_list = [["X", "X"], ["X", "O"], ["X", "O"], ["X", "X"]]
    correct = [["X", "X"], ["X", "O"], ["X", "O"], ["X", "X"]]
    test_5 = [region_list, correct, test_string]

    test_string = "Case: No surrounds."
    region_list = [
        ["X", "X", "O", "X", "X", "X"],
        ["X", "O", "O", "O", "X", "X"],
        ["X", "O", "O", "O", "X", "X"],
        ["X", "O", "O", "X", "X", "X"],
        ["X", "X", "X", "O", "X", "X"],
        ["X", "O", "X", "O", "X", "O"],
    ]
    correct = [
        ["X", "X", "O", "X", "X", "X"],
        ["X", "O", "O", "O", "X", "X"],
        ["X", "O", "O", "O", "X", "X"],
        ["X", "O", "O", "X", "X", "X"],
        ["X", "X", "X", "O", "X", "X"],
        ["X", "O", "X", "O", "X", "O"],
    ]
    test_6 = [region_list, correct, test_string]

    test_string = "Case: Regions only at edges of map."
    region_list = [
        ["X", "O", "O", "X", "X", "O"],
        ["X", "X", "X", "X", "X", "O"],
        ["O", "X", "X", "X", "X", "O"],
        ["X", "X", "X", "X", "X", "X"],
        ["O", "X", "X", "X", "X", "X"],
        ["O", "X", "X", "X", "X", "X"],
    ]
    correct = [
        ["X", "O", "O", "X", "X", "O"],
        ["X", "X", "X", "X", "X", "O"],
        ["O", "X", "X", "X", "X", "O"],
        ["X", "X", "X", "X", "X", "X"],
        ["O", "X", "X", "X", "X", "X"],
        ["O", "X", "X", "X", "X", "X"],
    ]
    test_7 = [region_list, correct, test_string]

    test_string = "Case: No regions."
    region_list = [
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
    ]
    correct = [
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
    ]
    test_8 = [region_list, correct, test_string]

    test_string = "Case: One big region in middle."
    region_list = [
        ["X", "X", "X", "X", "X", "X"],
        ["X", "O", "O", "O", "O", "X"],
        ["X", "O", "O", "O", "O", "X"],
        ["X", "O", "O", "O", "O", "X"],
        ["X", "O", "O", "O", "O", "X"],
        ["X", "X", "X", "X", "X", "X"],
    ]
    correct = [
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
    ]
    test_9 = [region_list, correct, test_string]

    test_string = "Case: Small regions 1."
    region_list = [
        ["X", "O", "X", "X", "X", "X"],
        ["X", "O", "X", "X", "O", "X"],
        ["X", "O", "X", "X", "X", "X"],
        ["X", "O", "X", "O", "X", "X"],
        ["X", "O", "X", "O", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
    ]
    correct = [
        ["X", "O", "X", "X", "X", "X"],
        ["X", "O", "X", "X", "X", "X"],
        ["X", "O", "X", "X", "X", "X"],
        ["X", "O", "X", "X", "X", "X"],
        ["X", "O", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
    ]
    test_10 = [region_list, correct, test_string]

    test_string = "Case: Small regions 2."
    region_list = [
        ["X", "X", "X", "X", "X", "X"],
        ["X", "O", "X", "X", "O", "O"],
        ["X", "O", "X", "X", "X", "X"],
        ["X", "X", "X", "O", "X", "X"],
        ["X", "X", "O", "X", "X", "X"],
        ["X", "X", "X", "X", "O", "X"],
        ["O", "O", "X", "X", "X", "X"],
        ["X", "X", "O", "X", "O", "X"],
        ["X", "X", "O", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "O", "X", "O", "X", "X"],
        ["X", "X", "X", "O", "X", "X"],
        ["O", "O", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "O", "O"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "O", "X", "X", "X"],
        ["X", "X", "X", "X", "O", "X"],
        ["O", "O", "X", "X", "X", "X"],
    ]
    correct = [
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "O", "O"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["O", "O", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["O", "O", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "O", "O"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X"],
        ["O", "O", "X", "X", "X", "X"],
    ]
    test_11 = [region_list, correct, test_string]

    test_string = "Case: All region."
    region_list = [
        ["O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
    ]
    correct = [
        ["O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
    ]
    test_12 = [region_list, correct, test_string]

    test_string = "Case: Should return false case."
    region_list = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    correct = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "O", "X"],
    ]
    test_13 = [region_list, correct, test_string]
