"""Problem from LeetCode.com"""


class TreeNode:
    """Class from LeetCode.com."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Problem from LeetCode.com"""

    def path_sum(self, root: TreeNode, target_sum: int) -> int:
        """
        Count the number of paths within the tree that sum to our given target.

        Args:
            `root`: The top of the binary tree.
            `target_sum`: The target integer that we're searching for.
        Returns:
            `count`: The number of paths within the tree that sum to target.
        """

        # A total count shared in scope.
        self.total = 0

        # If empty tree
        if root is None:
            return 0

        def find_total_matches(node: TreeNode, sum: int):
            """
            Find the total matches beginning at this node.

            Uses the instance variable to store value.

            Args:
                `node`: The current node.
                `sum`: The sum to this point.
            """

            # If empty node
            if node is None:
                return
            # If correct sum
            if sum == target_sum:
                self.total += 1
            # Look at left and right child
            if node.left:
                find_total_matches(node.left, sum + node.left.val)
            if node.right:
                find_total_matches(node.right, sum + node.right.val)

        def in_order(node: TreeNode):
            """Traverse the tree to apply other function on each node."""
            if node:
                find_total_matches(node, node.val)
                in_order(node.left)
                in_order(node.right)

        # Traverse the tree
        in_order(root)

        # Return the total found paths
        return self.total
