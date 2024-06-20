"""Holds some input cases and results to be run"""

from tree_node import TreeNode


class TestCases:
    """A collection of test cases and solutions for maximum_depth_of_binary_tree.py tests"""

    a = TreeNode(7)
    b = TreeNode(15)
    c = TreeNode(29, b, a)
    d = TreeNode(9)
    test_1_head = TreeNode(3, d, c)
    solution_1 = 3

    f = TreeNode(2)
    test_2_head = TreeNode(1, a)
    solution_2 = 2

    test_3_head = TreeNode(2)
    solution_3 = 1

    test_4_head = None
    solution_4 = 0
