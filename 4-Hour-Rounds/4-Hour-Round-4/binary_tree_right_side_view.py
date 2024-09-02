"""Problem from LeetCode.com"""


class TreeNode:
    """Class from LeetCode.com."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """Problem from LeetCode.com"""

    def __init__(self):
        self.output = []
        self.output_depth = 0

    def right_side_view(self, root: TreeNode) -> list[int]:
        """
        Finds a list of values of the binary tree as if looking from the right
        side.

        Args:
            `root`: The top node of the tree.
        Returns:
            `self.output`: A List of the right-most nodes in the tree.
        """

        # Handle edge-cases.
        if root is None:
            return None
        if root.left is None and root.right is None:
            return [root.val]

        # Build the list.
        self.right_side_traversal(root, 0)
        return self.output

    def right_side_traversal(self, root: TreeNode, depth: int):
        """
        Performs the right traversal to build a list of the right-most nodes, `self.output`.

        Args:
            `root`: The current node.
            `depth`: The depth of the current node.
        """

        # If the current node's depth is now deepest seen, add it.
        depth += 1
        if depth > self.output_depth:
            print(f"Added {root.val}")
            self.output.append(root.val)
            self.output_depth += 1

        # Step into left and right children.
        if root.right is not None:
            self.right_side_traversal(root.right, depth)
        if root.left is not None:
            self.right_side_traversal(root.left, depth)
