""" This module holds a function to return the binary tree of a given preorder and inorder traversal representation of the tree """

from tree_node import TreeNode

# pylint: disable=C0301


class Solution:
    """Given class by LeetCode to perform methods in"""

    def build_tree_1(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        """
        Returns the binary tree of a given preorder and inorder traversal representation of the tree.

        Args:
            `preorder`: A list of integers that represents the preorder traversal of a given binary tree.
            `inorder`: A list of integers that represents the inorder traversal of a given binary tree.
        Returns:
            `TreeNode`: A ListNode object that is the head of a created binary tree from these descriptions.
        """

        head = TreeNode(preorder[0], None, None)

        if len(inorder[: inorder.index(preorder[0])]) > 0:
            head.left = TreeNode(preorder[1], None, None)
            new_inorder = inorder[: inorder.index(preorder[0])]
            new_preorder = preorder[1 : 1 + len(new_inorder)]
            self.recursive_builder(new_preorder, new_inorder, head.left)
        if len(inorder[inorder.index(preorder[0]) + 1 :]) > 0:
            new_inorder = inorder[inorder.index(preorder[0]) + 1 :]
            new_preorder = preorder[-len(new_inorder) :]
            head.right = TreeNode(new_preorder[0], None, None)
            self.recursive_builder(new_preorder, new_inorder, head.right)

        return head

    def recursive_builder(
        self, preorder: list[int], inorder: list[int], new_node: TreeNode
    ):
        """Recursively builds a node tree given a pre-ordered and inorder set of lists of a binary tree."""

        # If there are numbers to the left of our number in "inorder"
        if len(inorder[: inorder.index(preorder[0])]) > 0:
            new_node.left = TreeNode(preorder[1], None, None)
            new_inorder = inorder[: inorder.index(preorder[0])]
            new_preorder = preorder[1 : 1 + len(new_inorder)]
            self.recursive_builder(new_preorder, new_inorder, new_node.left)

        # If there are numbers to the right of our number
        if len(inorder[inorder.index(preorder[0]) + 1 :]) > 0:
            new_inorder = inorder[inorder.index(preorder[0]) + 1 :]
            new_preorder = preorder[-len(new_inorder) :]
            new_node.right = TreeNode(new_preorder[0], None, None)
            self.recursive_builder(new_preorder, new_inorder, new_node.right)

        return
