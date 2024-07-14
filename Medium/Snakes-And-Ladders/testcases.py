"""A collection of test cases and solutions for `snakes_and_ladders.py` tests."""

import random


class TestCases:
    """
    A collection of test cases and solutions for `snakes_and_ladders.py` tests.
    """

    test_string = "Case: Example case."
    test_list = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
    correct = 4
    test_1 = [test_list, correct, test_string]

    test_string = "Case: Example case 2."
    test_list = [[-1, -1], [-1, 3]]
    correct = 1
    test_2 = [test_list, correct, test_string]

    test_string = "Case: No shortcuts."
    test_list = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
    ]
    correct = 6
    test_3 = [test_list, correct, test_string]

    test_string = "Case: Shortcut."
    test_list = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, -1, -1],
    ]
    correct = 2
    test_4 = [test_list, correct, test_string]

    test_string = "Case: Impossible."
    test_list = [
        [-1, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
    ]
    correct = -1
    test_5 = [test_list, correct, test_string]

    test_string = "Case: Possible only if taking ladder."
    test_list = [
        [-1, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 34, -1, -1],
    ]
    correct = 2
    test_6 = [test_list, correct, test_string]

    test_string = "Case: Must miss all snakes."
    test_list = [
        [-1, 2, 2, 2, 2, -1],
        [-1, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, -1],
        [-1, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, -1],
        [-1, 2, 2, 2, 2, 2],
    ]
    correct = 6
    test_7 = [test_list, correct, test_string]

    test_string = "Case: Something back and forth."
    test_list = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, 9],
        [-1, -1, 35, -1, 2, 2],
        [-1, 17, 2, 2, 2, 2],
    ]
    correct = 4
    test_8 = [test_list, correct, test_string]

    # If they did stack, this is 2
    # Hitting 29>35, then walking is 3
    # Passing the 29, then walking to next 35 is 4.
    # Correct = 3
    test_string = "Case: Ladders don't stack."
    test_list = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, 35, -1],
        [-1, -1, -1, -1, -1, 35],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, 29],
        [-1, -1, -1, -1, -1, -1],
    ]
    correct = 3
    test_9 = [test_list, correct, test_string]

    test_string = "Case: Longer case, must walk all the way."
    t_list = []
    test_list = []
    for i in range(0, 20):
        t_list.append(-1)
    for j in range(0, 20):
        test_list.append(t_list)
    correct = 67
    test_10 = [test_list, correct, test_string]

    test_string = "Case: Ladder can take us to last position."
    test_list = [
        [-1, -1, 19, 10, -1],
        [2, -1, -1, 6, -1],
        [-1, 17, -1, 19, -1],
        [25, -1, 20, -1, -1],
        [-1, -1, -1, -1, 15],
    ]
    correct = 2
    test_11 = [test_list, correct, test_string]

    test_string = "Case: Example from discussion board. Forward, backward."
    test_list = [[-1, 1, 2, -1], [2, 13, 15, -1], [-1, 10, -1, -1], [-1, 6, 2, 8]]
    correct = 2
    test_12 = [test_list, correct, test_string]

    test_string = "Case: Time-limit Exceeded."
    test_list = [
        [-1, 5, -1, -1, 17, 6, -1],
        [41, 28, -1, -1, -1, 27, -1],
        [35, 42, -1, -1, -1, -1, 4],
        [7, 32, -1, 25, -1, 43, -1],
        [-1, 26, 5, -1, -1, -1, 25],
        [28, -1, -1, 5, -1, -1, 41],
        [-1, 42, 28, 25, -1, 7, 28],
    ]
    correct = 3
    test_13 = [test_list, correct, test_string]
