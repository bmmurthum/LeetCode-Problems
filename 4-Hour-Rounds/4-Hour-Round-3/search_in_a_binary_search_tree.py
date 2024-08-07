"""Problem from LeetCode.com"""


class TreeNode:
    """Class from LeetCode.com."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Problem from LeetCode.com"""

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Searches a binary tree for a node with the value that matches `val`,
        then returns the tree from that node.

        Args:
            `root`: The top of our given tree.
            `val`: The target value to look for in a node.
        Returns:
            `new_root`: A root node of a subtree to return.
        """

        # If this root has the value we're searching for, return this pointer.
        if root.val == val:
            return root

        # Look at left and right child.
        new_root = None
        if root.left is not None:
            a = self.searchBST(root.left, val)
            if a is not None:
                new_root = a
        if root.right is not None:
            b = self.searchBST(root.right, val)
            if b is not None:
                new_root = b
        return new_root
