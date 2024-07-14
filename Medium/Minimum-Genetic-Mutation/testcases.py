"""A collection of test cases and solutions for `minimum_genetic_mutation.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `minimum_genetic_mutation.py` tests.
    """

    test_string = "Case: Example case."
    test_start = "AACCGGTT"
    test_end = "AACCGGTA"
    test_list = ["AACCGGTA"]
    correct = 1
    test_1 = [test_start, test_end, test_list, correct, test_string]

    test_string = "Case: Example case 2."
    test_start = "AACCGGTT"
    test_end = "AAACGGTA"
    test_list = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    correct = 2
    test_2 = [test_start, test_end, test_list, correct, test_string]

    test_string = "Case: Never finds goal."
    test_start = "AACCGGTT"
    test_end = "AAACGGTA"
    test_list = ["GGGGGGGG", "CCCCCCCC", "AAAAAAAA"]
    correct = -1
    test_3 = [test_start, test_end, test_list, correct, test_string]

    test_string = "Case: Takes several steps."
    test_start = "AAAAAAAA"
    test_end = "GAGTGGAC"
    test_list = [
        "AAAAAAAC",
        "AGAAAAAA",
        "AGCAAAAA",
        "AAAAAAGC",
        "AAAAAGGC",
        "AAAAGGGC",
        "AAATGGGC",
        "AAATGGAC",
        "AAGTGGAC",
        "GAGTGGAC",
    ]
    correct = 8
    test_4 = [test_start, test_end, test_list, correct, test_string]

    test_string = "Case: Takes two steps. There is another false path."
    test_start = "AAAAAAAA"
    test_end = "AGCAAAAA"
    test_list = [
        "AAAAAAAC",
        "AGAAAAAA",
        "AGCAAAAA",
        "AAAAAAGC",
        "AAAAAGGC",
        "AAAAGGGC",
        "AAATGGGC",
        "AAATGGAC",
        "AAGTGGAC",
        "GAGTGGAC",
    ]
    correct = 2
    test_5 = [test_start, test_end, test_list, correct, test_string]
