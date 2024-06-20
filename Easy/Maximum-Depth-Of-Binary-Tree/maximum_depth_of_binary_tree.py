""" This module holds a function to return the max-depth of a binary tree """

from tree_node import TreeNode


class Solution:
    """Given class by LeetCode to perform methods in"""

    def max_depth_1(self, root: TreeNode) -> int:
        """Returns the maximum depth of a binary tree from the `root` node."""

        if root is None:
            return 0
        left_max = self.max_depth_1(root.left)
        right_max = self.max_depth_1(root.right)
        maximum = max(left_max, right_max)
        return maximum + 1
