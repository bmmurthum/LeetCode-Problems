""" This module holds a function to return the max-depth of a binary tree """

from tree_node import TreeNode


class Solution:
    """Given class by LeetCode to perform methods in"""

    def max_depth_2(self, root: TreeNode) -> int:
        """Returns the maximum depth of a binary tree from the `root` node."""

        if root is None:
            return 0
        else:
            return max(self.max_depth_2(root.left), self.max_depth_2(root.right)) + 1
