"""A collection of test cases and solutions for `path_sum.py` tests."""

from list_to_binary_tree import list_to_binary_tree


class TestCases:
    """A collection of test cases and solutions for `path_sum.py` tests."""

    # Test 1 - Target not found

    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7

    tree_list = [3, 9, 20, None, None, 15, 7]
    tree_as_nodes = list_to_binary_tree(tree_list)
    target_sum = 11
    correct = False
    test_1 = [tree_as_nodes, target_sum, correct]

    # Test 2 - One on bottom depth

    #         1
    #       /    \
    #      2      3
    #     / \    / \
    #    4   5  6   7
    #   /
    #  8

    tree_list = [1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, None]
    tree_as_nodes = list_to_binary_tree(tree_list)
    target_sum = 15
    correct = True
    test_2 = [tree_as_nodes, target_sum, correct]

    # Test 3 - Full tree. Two solutions possible.

    #              1
    #        /            \
    #       2              3
    #     /    \         /     \
    #    4      5       6       7
    #   / \    /  \    /  \    /  \
    #  8   9  10  14  12  13  14  15

    tree_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 12, 13, 14, 15]
    tree_as_nodes = list_to_binary_tree(tree_list)
    target_sum = 22
    correct = True
    test_3 = [tree_as_nodes, target_sum, correct]

    # Test 4 - Only left children

    #         1
    #       /
    #      2
    #     /
    #    3
    #   /
    #  4

    tree_list = [
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
    tree_as_nodes = list_to_binary_tree(tree_list)
    target_sum = 10
    correct = True
    test_4 = [tree_as_nodes, target_sum, correct]

    # Test 5 - Right children only. Negative total.

    #       1
    #        \
    #         -2
    #          \
    #           -3
    #            \
    #             -4

    tree_list = [
        1,
        None,
        -2,
        None,
        None,
        None,
        -3,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        -4,
    ]
    tree_as_nodes = list_to_binary_tree(tree_list)
    target_sum = -8
    correct = True
    test_5 = [tree_as_nodes, target_sum, correct]

    # Test 6 - Single Node

    #       2
    #     /   \
    #   __     __

    tree_list = [2]
    tree_as_nodes = list_to_binary_tree(tree_list)
    target_sum = 2
    correct = True
    test_6 = [tree_as_nodes, target_sum, correct]

    # Test 7 - Two nodes. Negative node-value.

    #       -1
    #     /   \
    #   10     __

    tree_list = [-1, 10, None]
    tree_as_nodes = list_to_binary_tree(tree_list)
    target_sum = 9
    correct = True
    test_7 = [tree_as_nodes, target_sum, correct]

    # Test 8 - All zeroes.

    #     0
    #    / \
    #   0   0
    #      / \
    #     0   0

    tree_list = [0, 0, 0, None, None, 0, 0]
    tree_as_nodes = list_to_binary_tree(tree_list)
    target_sum = 0
    correct = True
    test_8 = [tree_as_nodes, target_sum, correct]

    # Test 9 - Empty list.

    tree_list = []
    tree_as_nodes = None
    target_sum = 2
    correct = False
    test_9 = [tree_as_nodes, target_sum, correct]
