""" Someone else's solution. For comparison in performance. """

from tree_node import TreeNode


class Solution:
    def __init__(self):
        self.isValid = False

    def findPathSum(self, root, total, curr_sum):
        if root is None:
            return 0

        if self.isValid == True:
            return self.isValid

        curr_sum += root.val

        if root.left == None and root.right == None:
            # leaf node found
            if curr_sum == total:
                self.isValid = True
        else:
            self.findPathSum(root.left, total, curr_sum)
            self.findPathSum(root.right, total, curr_sum)

    def has_path_sum_2(self, root: TreeNode, targetSum: int) -> bool:
        self.findPathSum(root, targetSum, 0)
        return 1 if self.isValid else 0
