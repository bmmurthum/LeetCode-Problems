""" A helper class to our implementation of a binary tree """


class TreeNode:
    """A simple node object, "leaf", within a binary tree. Given by LeetCode."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
