"""A collection of test cases and solutions for `rotate_image.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `rotate_image.py` tests.
    """

    test_string = "Case: Example 1."
    test_input_1 = "egg"
    test_input_2 = "add"
    correct = True
    test_1 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Example 2."
    test_input_1 = "foo"
    test_input_2 = "bar"
    correct = False
    test_2 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Example 3."
    test_input_1 = "paper"
    test_input_2 = "title"
    correct = True
    test_3 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Single letter."
    test_input_1 = "a"
    test_input_2 = "b"
    correct = True
    test_4 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Lowercase and uppercase being different."
    test_input_1 = "cat"
    test_input_2 = "CAT"
    correct = True
    test_5 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Using other ASCII characters."
    test_input_1 = "apple"
    test_input_2 = "@&&13"
    correct = True
    test_6 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Whole alphabet."
    test_input_1 = "abcdefghijklmnopqrstuvwxyz"
    test_input_2 = "cdefghijklmnopqrstuvwxyzab"
    correct = True
    test_7 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Whole alphabet, twice."
    test_input_1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    test_input_2 = "cdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzab"
    correct = True
    test_8 = [test_input_1, test_input_2, correct, test_string]

    test_string = "Case: Whole alphabet, twice. Last letter wrong."
    test_input_1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzz"
    test_input_2 = "cdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabc"
    correct = False
    test_9 = [test_input_1, test_input_2, correct, test_string]
