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
        self.path = []

    def lowest_common_ancestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """
        Finds the lowest common ancestor of two target nodes in a binary tree.

        Args:
            `root`: The top node of our tree.
            `p`: One target node.
            `q`: The other target node.
        Returns:
            `current_node`: The shared ancestor node.
        """

        # Find a path to the first node
        self.path = self.recursive_path_find(root, p, self.path)

        # Starting at bottom of path, see if we can find the second node by
        # following children from the current node.
        for i in range(len(self.path) - 1, -1, -1):
            current_node = self.path[i]
            if current_node.left is not None or current_node.right is not None:
                new_path = []
                result = self.recursive_path_find(current_node, q, new_path)
                if result is not None:
                    return current_node.val
        return root

    def recursive_path_find(self, node: TreeNode, target: TreeNode, path: list):
        """
        Returns the path to the target. If target not found, returns None.

        Args:
            `node`: The current node.
            `target`: The target node we're searching for.
            `path`: The current list of the nodes we've looked at to get here.
        Returns:
            `path`: The list of nodes to find the target. None, if not found.
        """

        # Add this node to path
        path.append(node)

        # If found the target, return out.
        if node == target:
            return path

        # Look left
        if node.left is not None and node.left not in self.path:
            temp = path.copy()
            new_path = self.recursive_path_find(node.left, target, temp)
        else:
            new_path = None
        if new_path is not None:
            return new_path

        # Look right
        if node.right is not None and node.right not in self.path:
            temp = path.copy()
            new_path = self.recursive_path_find(node.right, target, temp)
        else:
            new_path = None
        if new_path is not None:
            return new_path

        return None
