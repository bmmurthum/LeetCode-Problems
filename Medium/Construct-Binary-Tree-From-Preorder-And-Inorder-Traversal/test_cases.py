"""Holds some input cases and results to be run"""


class TestCases:
    """A collection of test cases and solutions for maximum_depth_of_binary_tree.py tests"""

    # Test 1

    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    correct = [3, 9, 20, None, None, 15, 7]
    test_1 = [preorder, inorder, correct]

    # Test 2

    #         1
    #       /    \
    #      2      3
    #     / \    / \
    #    4   5  6   7
    #   /
    #  8

    preorder = [1, 2, 4, 8, 5, 3, 6, 7]
    inorder = [8, 4, 2, 5, 1, 6, 3, 7]
    correct = [1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, None]
    test_2 = [preorder, inorder, correct]

    # Test 3

    #              1
    #        /            \
    #       2              3
    #     /    \         /     \
    #    4      5       6       7
    #   / \    /  \    /  \    /  \
    #  8   9  10  11  12  13  14  15

    preorder = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
    inorder = [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    test_3 = [preorder, inorder, correct]

    # Test 4

    #         1
    #       /
    #      2
    #     /
    #    3
    #   /
    #  4

    preorder = [1, 2, 3, 4]
    inorder = [4, 3, 2, 1]
    correct = [
        1,
        2,
        None,
        3,
        None,
        None,
        None,
        4,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    test_4 = [preorder, inorder, correct]

    # Test 5

    #       1
    #        \
    #         2
    #          \
    #           3
    #            \
    #             4

    preorder = [1, 2, 3, 4]
    inorder = [1, 2, 3, 4]
    correct = [
        1,
        None,
        2,
        None,
        None,
        None,
        3,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        4,
    ]
    test_5 = [preorder, inorder, correct]

    # Test 6

    #       2
    #     /   \
    #   __     __

    preorder = [2]
    inorder = [2]
    correct = [2]
    test_6 = [preorder, inorder, correct]

    # Test 7

    #       -1
    #     /   \
    #   10     __

    preorder = [-1, 10]
    inorder = [10, -1]
    correct = [-1, 10, None]
    test_7 = [preorder, inorder, correct]

    # Test 8

    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    false = [3, 9, 20, 15, None, None, None]
    test_8 = [preorder, inorder, false]
