""" This module holds the function to output a binary node tree as a list """

from tree_node import TreeNode


def display_tree_as_list(head: TreeNode) -> list:
    """Returns a list display of the binary node tree"""

    new_list = []
    new_list_length = 2 ** max_depth(head)
    for _ in range(0, new_list_length - 1):
        new_list.append(None)

    display_tree_helper(head, 0, new_list)

    return new_list


def display_tree_helper(head: TreeNode, position_value: int, new_list: list):
    """Returns a list implementation of the node-tree, for testing"""
    new_list[position_value] = head.val
    if head.left is not None:
        left_position_value = position_value * 2 + 1
        display_tree_helper(head.left, left_position_value, new_list)
    if head.right is not None:
        right_position_value = position_value * 2 + 2
        display_tree_helper(head.right, right_position_value, new_list)


def max_depth(root: TreeNode) -> int:
    """Returns the maximum depth of a binary tree from the `root` node."""

    if root is None:
        return 0
    left_max = max_depth(root.left)
    right_max = max_depth(root.right)
    maximum = max(left_max, right_max)
    return maximum + 1
