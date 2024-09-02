"""Problem from LeetCode.com"""


class TreeNode:
    """Class from LeetCode.com."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Problem from LeetCode.com"""

    def max_level_sum(self, root: TreeNode) -> int:
        """
        Look for a depth, "level", of nodes that has the maximum sum of values.
        Top node represents "level 1", its children being "level 2."

        Args:
            `root`: The top node of the binary tree.
        Returns:
            `max_level`: The level of the tree with the max sum.
        """

        max_level = 1
        max_sum = root.val
        current_level_nodes = []
        current_level_nodes.append(root)
        current_level = 1
        while len(current_level_nodes) > 0:
            # Check current level's sum against max
            current_level_sum = self.sum_of_node_values(current_level_nodes)
            if current_level_sum > max_sum:
                max_sum = current_level_sum
                max_level = current_level
            # Iterate to next level
            temp = []
            for node in current_level_nodes:
                if node.left is not None:
                    temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)
            current_level_nodes = temp
            current_level += 1

        return max_level

    def sum_of_node_values(self, node_list) -> int:
        """Returns the sum of the list of nodes."""
        sum = 0
        for node in node_list:
            sum += node.val
        return sum
