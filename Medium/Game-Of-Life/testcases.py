"""A collection of test cases and solutions for `rotate_image.py` tests."""


class TestCases:
    """
    A collection of test cases and solutions for `rotate_image.py` tests.
    """

    #  0 1 0     0 0 0
    #  0 0 1     1 0 1
    #  1 1 1  >  0 1 1
    #  0 0 0     0 1 0
    test_string = "Case: Example case."
    test_input = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    correct = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    test_1 = [test_input, correct, test_string]

    #  1 1     1 1
    #  1 0  >  1 1
    test_string = "Case: Example case 2."
    test_input = [[1, 1], [1, 0]]
    correct = [[1, 1], [1, 1]]
    test_2 = [test_input, correct, test_string]

    #  1 1 1 1     1 0 0 1
    #  1 1 1 1  >  0 0 0 0
    #  1 1 1 1     1 0 0 1
    test_string = "Case: 4x3 all 1s."
    test_input = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    correct = [[1, 0, 0, 1], [0, 0, 0, 0], [1, 0, 0, 1]]
    test_3 = [test_input, correct, test_string]

    #  1 0 1     0 0 0
    #  1 0 1  >  1 0 1
    #  1 0 1     0 0 0
    test_string = "Case: 3x3."
    test_input = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    correct = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    test_4 = [test_input, correct, test_string]

    #  0 0 0     0 0 0
    #  0 0 0  >  0 0 0
    #  0 0 0     0 0 0
    test_string = "Case: 3x3 all 0s."
    test_input = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    correct = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    test_5 = [test_input, correct, test_string]

    test_string = "Case: 1x1."
    test_input = [[1]]
    correct = [[0]]
    test_6 = [test_input, correct, test_string]

    test_string = "Case: 1x1."
    test_input = [[0]]
    correct = [[0]]
    test_7 = [test_input, correct, test_string]

    test_string = "Case: 1x3."
    test_input = [[1, 1, 1]]
    correct = [[0, 1, 0]]
    test_8 = [test_input, correct, test_string]

    test_string = "Case: 1x3."
    test_input = [[0, 1, 0]]
    correct = [[0, 0, 0]]
    test_9 = [test_input, correct, test_string]

    #  1 1 0 1 0 1 0 1 1 0      1 1 0 0 1 0 1 1 0 1
    #  1 1 0 1 0 0 0 1 1 1      0 0 0 1 0 1 0 0 0 1
    #  1 1 0 0 1 0 1 0 0 0      0 0 0 1 1 0 1 0 0 1
    #  1 0 0 1 0 1 1 0 0 1      1 0 0 0 0 0 1 1 1 0
    #  0 0 1 1 1 0 0 1 0 1  >   1 0 1 0 0 0 0 1 0 1
    #  1 1 0 0 1 0 0 1 1 0      1 0 0 0 1 1 1 1 0 1
    #  0 1 1 1 0 0 1 0 0 1      0 0 0 1 0 0 0 0 0 1
    #  0 1 0 0 0 0 0 0 1 1      0 0 0 0 0 1 1 0 0 1
    #  1 1 1 0 1 0 1 1 0 1      0 0 0 0 1 0 1 0 0 0
    #  1 1 0 1 1 1 0 1 1 1      1 0 0 1 1 1 0 1 0 1
    test_string = "Case: 10x10."
    test_input = [
        [1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    ]
    correct = [
        [1, 1, 0, 0, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    ]
    test_10 = [test_input, correct, test_string]
