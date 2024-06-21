""" Someone else's solution """

from tree_node import TreeNode


class Solution:
    """Given class by LeetCode to perform methods in"""

    def recursion(self, i, j):
        if i > j:
            return None

        root_val = self.preorder[self.r]
        self.r += 1
        split_index = self.inorder_index[root_val]

        left = self.recursion(i, split_index - 1)
        right = self.recursion(split_index + 1, j)

        root = TreeNode(root_val, left, right)

        return root

    def build_tree_2(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        self.inorder_index = {v: i for i, v in enumerate(inorder)}
        self.inorder = inorder
        self.preorder = preorder
        self.r = 0
        i = 0
        j = len(inorder) - 1

        result = self.recursion(i, j)

        return result
