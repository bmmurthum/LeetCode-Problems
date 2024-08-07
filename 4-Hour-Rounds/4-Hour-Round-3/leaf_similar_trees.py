"""Problem from LeetCode.com"""


class TreeNode:
    """Class from LeetCode.com"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Problem from LeetCode.com"""

    def leaf_similar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Find whether two trees have the same leaf order of values.

        Args:
            `root1`: The top of one tree
            `root2`: The top of another tree
        Returns:
            `True/False`: If the leaf values are identical.
        """

        # Compare the two leaf lists that were generated
        leaf_order_1 = self.find_leaf_order(root1)
        leaf_order_2 = self.find_leaf_order(root2)
        if leaf_order_1 == leaf_order_2:
            return True
        return False

    def find_leaf_order(self, root: TreeNode) -> list[int]:
        """
        Uses depth-first search to generate a list of leaves.

        Args:
            `root`: The current root branch.
        Returns:
            `output`: The list of this branch and below's leaves.
        """

        # If None
        if root is None:
            return []
        # If leaf
        if root.left is None and root.right is None:
            return [root.val]
        # If not leaf
        else:
            output = []
            left = self.find_leaf_order(root.left)
            right = self.find_leaf_order(root.right)
            output += left
            output += right
            return output
