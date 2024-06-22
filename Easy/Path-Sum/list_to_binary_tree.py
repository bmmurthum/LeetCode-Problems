# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301

""" Module for the method of creating a node-tree from a list representation """

from tree_node import TreeNode


def list_to_binary_tree(our_list, node=None, index=0) -> TreeNode:
    """
    Takes a list representation of a binary tree and returns a node-connected version for traversal.

    Args:
        `list`: A list of integers that represents a given binary tree.
        `index`: The int index in the list of the current node looked-at while in traversal for creation.
    Returns:
        `node`: A TreeNode object that is the head of a created binary tree.
    """

    # Only calls this for the head initial creation.
    # node = None
    if index == 0:
        node = TreeNode(our_list[index], None, None)

    # Creates nodes when we know that we have valid children.
    # Then we step into that child as a new parent.
    new_left_index = index * 2 + 1
    new_right_index = index * 2 + 2
    if new_left_index < len(our_list) and our_list[new_left_index] is not None:
        node.left = TreeNode(our_list[new_left_index], None, None)
        list_to_binary_tree(our_list, node.left, new_left_index)
    if new_right_index < len(our_list) and our_list[new_right_index] is not None:
        node.right = TreeNode(our_list[new_right_index], None, None)
        list_to_binary_tree(our_list, node.right, new_right_index)

    # Only returns the head node.
    return node
