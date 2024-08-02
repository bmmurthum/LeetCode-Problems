"""A collection of test cases and solutions for `integer_to_roman.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `integer_to_roman.py` tests.
    """

    test_string = "Case: Example 1."
    test_input = 3749
    correct = "MMMDCCXLIX"
    test_1 = [test_input, correct, test_string]

    test_string = "Case: Example 2."
    test_input = 58
    correct = "LVIII"
    test_2 = [test_input, correct, test_string]

    test_string = "Case: Example 3."
    test_input = 1994
    correct = "MCMXCIV"
    test_3 = [test_input, correct, test_string]

    test_string = "Case: 1."
    test_input = 1
    correct = "I"
    test_4 = [test_input, correct, test_string]

    test_string = "Case: 2."
    test_input = 2
    correct = "II"
    test_5 = [test_input, correct, test_string]

    test_string = "Case: 3."
    test_input = 3
    correct = "III"
    test_6 = [test_input, correct, test_string]

    test_string = "Case: 4."
    test_input = 4
    correct = "IV"
    test_7 = [test_input, correct, test_string]

    test_string = "Case: 5."
    test_input = 5
    correct = "V"
    test_8 = [test_input, correct, test_string]

    test_string = "Case: 6."
    test_input = 6
    correct = "VI"
    test_9 = [test_input, correct, test_string]

    test_string = "Case: 7."
    test_input = 7
    correct = "VII"
    test_10 = [test_input, correct, test_string]

    test_string = "Case: 8."
    test_input = 8
    correct = "VIII"
    test_11 = [test_input, correct, test_string]

    test_string = "Case: 9."
    test_input = 9
    correct = "IX"
    test_12 = [test_input, correct, test_string]

    test_string = "Case: 10."
    test_input = 10
    correct = "X"
    test_13 = [test_input, correct, test_string]

    test_string = "Case: 3999."
    test_input = 3999
    correct = "MMMCMXCIX"
    test_14 = [test_input, correct, test_string]

    test_string = "Case: 3998."
    test_input = 3998
    correct = "MMMCMXCVIII"
    test_15 = [test_input, correct, test_string]

    test_string = "Case: 1111."
    test_input = 1111
    correct = "MCXI"
    test_16 = [test_input, correct, test_string]

    test_string = "Case: 555."
    test_input = 555
    correct = "DLV"
    test_17 = [test_input, correct, test_string]

    test_string = "Case: 666."
    test_input = 666
    correct = "DCLXVI"
    test_18 = [test_input, correct, test_string]
