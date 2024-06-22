from tree_node import TreeNode


class Solution:

    def has_path_sum_3(self, root: TreeNode, targetSum: int) -> bool:
        def go(node, acc):
            if node:
                if not node.left and not node.right:
                    if acc + node.val == targetSum:
                        return True
                    else:
                        return False
                else:
                    return go(node.left, acc + node.val) or go(
                        node.right, acc + node.val
                    )
            else:
                return False

        return go(root, 0)
