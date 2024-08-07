"""Problem from LeetCode.com"""


class TreeNode:
    """Class from LeetCode.com."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Problem from LeetCode.com"""

    def longest_zig_zag(self, root: TreeNode) -> int:
        """
        Handles finding the largest zigzag path in the tree.

        Args:
            `root`: The target node to look at.
        Returns:
            `count`: The largest zig-zag found.
        """

        left = 0
        right = 0
        if root.left:
            left = self.zig(root.left, "left", 1)
        if root.right:
            right = self.zig(root.right, "right", 1)

        count = max(left, right)
        return count

    def zig(self, node: TreeNode, left_right: str, zig_count: int) -> int:
        """
        Performs the zagging. Counts as it iterates downward. Returns the max
        number found.

        Args:
            `node`: The current node.
            `left_right`: Whether we arrived to this node from left or right.
            `zig_count`: How many zags to this position.
        Return:
            `count`: The largest zig found at/beneath this node.
        """

        left = 1
        right = 1
        if node.left:
            if left_right == "right":
                left = self.zig(node.left, "left", zig_count + 1)
            else:
                left = self.zig(node.left, "left", 1)
        if node.right:
            if left_right == "left":
                right = self.zig(node.right, "right", zig_count + 1)
            else:
                right = self.zig(node.right, "right", 1)

        count = max(left, right, zig_count)
        return count
