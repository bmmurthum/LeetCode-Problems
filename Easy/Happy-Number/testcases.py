"""A collection of test cases and solutions for `rotate_image.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `rotate_image.py` tests.
    """

    # 19  > 1**2 + 9**2 == 82
    # 82  > 8**2 + 2**2 == 68
    # 68  > 6**2 + 8**2 == 100
    # 100 > 1**2 + 0 + 0 == 1
    # 1 STOP
    test_string = "Case: Example 1."
    test_input = 19
    correct = True
    test_1 = [test_input, correct, test_string]

    # 2 > 2**2 == 4
    # 4 > 4**2 == 16
    # 16 > 1**2 + 6**2 == 37
    # 37 > 3**2 + 7**2 == 58
    # 58 > 5**2 + 8**2 == 89
    # 89 > 8**2 + 9**2 == 145
    # 145 > 1**2 + 4**2 + 5**2 == 42
    # 42 > 4**2 + 2**2 == 20
    # 20 > 2**2 + 0 == 4
    # 4 STOP
    test_string = "Case: Example 2."
    test_input = 2
    correct = False
    test_2 = [test_input, correct, test_string]

    # 1 STOP
    test_string = "Case: Sample."
    test_input = 1
    correct = True
    test_3 = [test_input, correct, test_string]

    # 3 > 3**2 == 9
    # 9 > 9**2 == 81
    # 81 > 8**2 + 1**2 == 65
    # 65 > 6**2 + 5**2 == 61
    # 61 > 6**2 + 1 == 37
    # 37 > 3**2 + 7**2 == 58
    # 58 > 5**2 + 8**2 == 89
    # 89 > 8**2 + 9**2 == 145
    # 145 > 1**2 + 4**2 + 5**2 == 42
    # 42 > 4**2 + 2**2 == 20
    # 20 > 2**2 + 0 == 4
    # 4 > 4**2 == 16
    # 16 > 1**2 + 6**2 == 37
    # 37 STOP
    test_string = "Case: Sample."
    test_input = 3
    correct = False
    test_4 = [test_input, correct, test_string]

    # 4 > 4**2 == 16
    # 16 > 1**2 + 6**2 == 37
    # 37 > 3**2 + 7**2 == 58
    # 58 > 5**2 + 8**2 == 89
    # 89 > 8**2 + 9**2 == 145
    # 145 > 1**2 + 4**2 + 5**2 == 42
    # 42 > 4**2 + 2**2 == 20
    # 20 > 2**2 + 0 == 4
    # 4 STOP
    test_string = "Case: Sample."
    test_input = 4
    correct = False
    test_5 = [test_input, correct, test_string]

    # 5 > 5**2 == 25
    # 25 > 2**2 + 5**2 == 29
    # 29 > 2**2 + 9**2 == 85
    # 85 > 8**2 + 5**2 == 89
    # 89 > 8**2 + 9**2 == 145
    # 145 > 1**2 + 4**2 + 5**2 == 42
    # 42 > 4**2 + 2**2 == 20
    # 20 > 2**2 + 0 == 4
    # 4 > 4**2 == 16
    # 16 > 1**2 + 6**2 == 37
    # 37 > 3**2 + 7**2 == 58
    # 58 > 5**2 + 8**2 == 89
    # 89 STOP
    test_string = "Case: Sample."
    test_input = 5
    correct = False
    test_6 = [test_input, correct, test_string]

    # 6 > 6**2 == 36
    # 36 > 3**2 + 6**2 == 45
    # 45 > 4**2 + 5**2 == 41
    # 41 > 4**2 + 1 == 17
    # 17 > 1 + 7**2 == 50
    # 50 > 5**2 + 0 == 25
    # 25 > 2**2 + 5**2 == 29
    # 29 > 2**2 + 9**2 == 85
    # 85 > 8**2 + 5**2 == 89
    # 89 > 8**2 + 9**2 == 145
    # 145 > 1**2 + 4**2 + 5**2 == 42
    # 42 > 4**2 + 2**2 == 20
    # 20 > 2**2 + 0 == 4
    # 4 > 4**2 == 16
    # 16 > 1**2 + 6**2 == 37
    # 37 > 3**2 + 7**2 == 58
    # 58 > 5**2 + 8**2 == 89
    # 89 STOP
    test_string = "Case: Sample."
    test_input = 6
    correct = False
    test_7 = [test_input, correct, test_string]

    # 7 > 7**2 == 49
    # 49 > 4**2 + 9**2 == 97
    # 97 > 9**2 + 7**2 == 130
    # 130 > 1 + 3**2 + 0 == 10
    # 10 > 1 + 0 == 1
    # 1 STOP
    test_string = "Case: Sample."
    test_input = 7
    correct = True
    test_8 = [test_input, correct, test_string]

    # 8 > 8**2 == 64
    # 64 > 6**2 + 4**2 == 52
    # 52 > 5**2 + 2**2 == 29
    # 29 > 2**2 + 9**2 == 85
    # 85 > 8**2 + 5**2 == 89
    # 89 > 8**2 + 9**2 == 145
    # 145 > 1**2 + 4**2 + 5**2 == 42
    # 42 > 4**2 + 2**2 == 20
    # 20 > 2**2 + 0 == 4
    # 4 > 4**2 == 16
    # 16 > 1**2 + 6**2 == 37
    # 37 > 3**2 + 7**2 == 58
    # 58 > 5**2 + 8**2 == 89
    # 89 STOP
    test_string = "Case: Sample."
    test_input = 8
    correct = False
    test_9 = [test_input, correct, test_string]

    # 9 > 9**2 == 81
    # 81 > 8**2 + 1 == 65
    # 65 KNOWN STOP
    test_string = "Case: Sample."
    test_input = 9
    correct = False
    test_10 = [test_input, correct, test_string]

    # 10 > 1 + 0 == 1
    # 1 STOP
    test_string = "Case: Sample."
    test_input = 10
    correct = True
    test_11 = [test_input, correct, test_string]

    # 11 > 1 + 1 == 2
    # 2 > 2**2 == 4
    # 4 > 4**2 == 16
    # 16 > 1**2 + 6**2 == 37
    # 37 > 3**2 + 7**2 == 58
    # 58 > 5**2 + 8**2 == 89
    # 89 > 8**2 + 9**2 == 145
    # 145 > 1**2 + 4**2 + 5**2 == 42
    # 42 > 4**2 + 2**2 == 20
    # 20 > 2**2 + 0 == 4
    # 4 STOP
    test_string = "Case: Sample."
    test_input = 11
    correct = False
    test_12 = [test_input, correct, test_string]

    # 12 > 1 + 2**2 == 5
    # 5 KNOWN STOP
    test_string = "Case: Sample."
    test_input = 12
    correct = False
    test_13 = [test_input, correct, test_string]

    # 13 > 1 + 3**2 == 10
    # 10 > 1 + 0 == 1
    # 1 STOP
    test_string = "Case: Sample."
    test_input = 13
    correct = True
    test_14 = [test_input, correct, test_string]

    # 14 > 1 + 4**2 == 17
    # 17 > 1 + 7**2 == 50
    # 50 KNOWN STOP
    test_string = "Case: Sample."
    test_input = 14
    correct = False
    test_15 = [test_input, correct, test_string]

    # 15 > 1 + 5**2 == 26
    # 26 > 2**2 + 6**2 == 40
    # 40 > 4**2 + 0 == 16
    # 16 KNOWN STOP
    test_string = "Case: Sample."
    test_input = 15
    correct = False
    test_16 = [test_input, correct, test_string]

    # 16 KNOWN STOP
    test_string = "Case: Sample."
    test_input = 16
    correct = False
    test_17 = [test_input, correct, test_string]

    # 17 KNOWN STOP
    test_string = "Case: Sample."
    test_input = 17
    correct = False
    test_18 = [test_input, correct, test_string]

    # 18 > 1 + 8**2 == 65
    # 65 KNOWN STOP
    test_string = "Case: Sample."
    test_input = 18
    correct = False
    test_19 = [test_input, correct, test_string]

    # 20 > 2**2 + 0 == 4
    # 4 KNOWN STOP
    test_string = "Case: Sample."
    test_input = 20
    correct = False
    test_20 = [test_input, correct, test_string]

    # 4909 > 4**2 + 9**2 + 0 + 9**2 == 178
    # 178 > 1 + 7**2 + 8**2 == 113
    # 113 > 1 + 1 + 3**2 == 11
    # 11 KNOWN STOP
    test_string = "Case: Random Number in Thousands."
    test_input = 4909
    correct = False
    test_21 = [test_input, correct, test_string]

    # 6585 > 6**2 + 5**2 + 8**2 + 5**2 == 150
    # 150 > 1 + 5**2 + 0 == 26
    # 26 KNOWN STOP
    test_string = "Case: Random Number in Thousands."
    test_input = 6585
    correct = False
    test_22 = [test_input, correct, test_string]

    # 3036 > 3**2 + 0 + 3**2 + 6**2 == 54
    # 54 > 5**2 + 4**2 == 41
    # 41 KNOWN STOP
    test_string = "Case: Random Number in Thousands."
    test_input = 3036
    correct = False
    test_23 = [test_input, correct, test_string]

    # 934063 > 9**2 + 3**2 + 4**2 + 0 + 6**2 + 3**2 == 151
    # 151 > 1 + 5**2 + 1 == 27
    # 27 > 2**2 + 7**2 == 53
    # 53 > 5**2 + 3**2 == 34
    # 34 > 3**2 + 4**2 == 25
    # 25 KNOWN STOP
    test_string = "Case: Random Number in Hundred Thousands."
    test_input = 934063
    correct = False
    test_24 = [test_input, correct, test_string]

    # 285916 > 2**2 + 8**2 + 5**2 + 9**2 + 1 + 6**2 == 211
    # 211 > 2**2 + 1 + 1 == 6
    # 6 KNOWN STOP
    test_string = "Case: Random Number in Hundred Thousands."
    test_input = 285916
    correct = False
    test_25 = [test_input, correct, test_string]

    # 434611 > 4**2 + 3**2 + 4**2 + 6**2 + 1 + 1 == 79
    # 79 > 7**2 + 9**2 == 130
    # 130 > 1 + 3**2 + 0 == 10
    # 10 > 1 + 0 == 1
    # 1 STOP
    test_string = "Case: Random Number in Hundred Thousands."
    test_input = 434611
    correct = True
    test_26 = [test_input, correct, test_string]
