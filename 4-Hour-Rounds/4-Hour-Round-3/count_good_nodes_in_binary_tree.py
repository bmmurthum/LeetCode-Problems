"""Problem from LeetCode.com"""


class TreeNode:
    """Class from LeetCode.com"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Problem from LeetCode.com"""

    def good_nodes(self, root: TreeNode) -> int:
        """
        Grab a count of nodes in which every parent older than it is equal to
        or lesser.

        Args:
            `root`: The top of the tree.
        """

        # Add totals from the left and right branches.
        # From there, do recursions to find totals.
        count = 1
        left = 0
        right = 0
        if root.left is not None:
            left = self.count_nodes_search(root.val, root.left)
        if root.right is not None:
            right = self.count_nodes_search(root.val, root.right)
        total = count + left + right
        return total

    def count_nodes_search(self, maximum_val: int, root: TreeNode) -> int:
        """
        Count how many child nodes from this node have a value greater than or
        equal to a given value.

        Args:
            `maximum_value`: A given value to check against.
            `root`: The current node to look at.
        Returns:
            `count`: A count of nodes.
        """

        count = 0
        # Check this node
        if root.val >= maximum_val:
            count += 1
            maximum_val = root.val
        # Check left
        left = 0
        if root.left is not None:
            left = self.count_nodes_search(maximum_val, root.left)
        # Check right
        right = 0
        if root.right is not None:
            right = self.count_nodes_search(maximum_val, root.right)
        # Add and return
        count += left + right
        return count
