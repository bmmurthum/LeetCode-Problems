# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201

""" This module holds the function for testing if a binary tree has a path with a given total sum. """

from tree_node import TreeNode


class Solution:
    """Provided class from LeetCode"""

    def has_path_sum_1(self, root: TreeNode, target_sum: int) -> bool:
        """Tells us if there is a path in the tree that sums to our value.

        Args:
            `root`: A `TreeNode` object that represents the head of the binary tree.
            `target_sum`: The value that we're looking for as a sum
        Returns:
            `bool`: True, if we found a path that sums to the total of `target_sum`
        """

        # Handle empty case
        if root is None:
            return False

        # Is able to look at this value within any level of recursion
        self.target_sum = target_sum

        # Start the search
        return self.recursive_search(root, 0)

    def recursive_search(self, node: TreeNode, cur_total: int) -> bool:
        """Looks through binary tree for a path that has our desired sum.

        Args:
            `node`: The TreeNode object that we're currently looking at.
            `cur_total`: The current total sum, before considering this node. Quickly changes to include this `node`.
        Returns:
            `bool`: True, if we found a path that sums to the total of `target_sum`
        Requirement:
            This function requires a value outside of function scope `target_sum` that each recursive level can see.
        """
        cur_total += node.val

        # If leaf, check to see if the sum is our desired sum
        if node.left is None and node.right is None:
            if cur_total == self.target_sum:
                return True
            else:
                return False
        # If not-leaf, has children.
        # If any child has returned True, we can stop searching.
        else:
            if node.left is not None:
                if self.recursive_search(node.left, cur_total):
                    return True
            if node.right is not None:
                if self.recursive_search(node.right, cur_total):
                    return True
            return False
