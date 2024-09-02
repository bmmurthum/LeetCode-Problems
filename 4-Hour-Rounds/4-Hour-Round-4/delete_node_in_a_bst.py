"""Problem from LeetCode.com"""


class TreeNode:
    """Class from LeetCode.com."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Problem from LeetCode.com"""

    def delete_node(self, root: TreeNode, key: int) -> TreeNode:
        """
        Remove a node from a binary search tree with a particular value. Return
        a root node to a new valid tree. If value is not found, return
        unaltered.

        Args:
            `root`: The root to a binary search tree.
            `key`: The value to look to remove.
        Return:
            `new_root`: Some given same/new root node.
        """

        # Handle edge-cases.
        if root is None:
            return None
        if root.val == key and root.left is None and root.right is None:
            return None
        if root.val == key:
            # If only one child
            if root.left is None and root.right is not None:
                return root.right
            elif root.right is None and root.left is not None:
                return root.left
            # If two children, put right children under left children.
            right_children = root.right
            new_root = root.left
            current = new_root
            while current.right is not None:
                current = current.right
            current.right = right_children
            return new_root

        # Look for our node to remove.
        last = None
        left_child = None
        right_child = None
        node_that_points_to_removed_left_or_right = None
        current = root
        while True:
            # If the key was not found, return tree unchanged.
            if current is None:
                return root
            # If we've found the key.
            if key == current.val:
                left_child = current.left
                right_child = current.right
                break
            # Iterate to next child.
            if key < current.val:
                last = current
                current = current.left
                node_that_points_to_removed_left_or_right = "left"
            elif key > current.val:
                last = current
                current = current.right
                node_that_points_to_removed_left_or_right = "right"
        node_that_points_to_removed = last
        node_to_remove = current

        # If we have a right child, find it's most-left child.
        # If not, if we have a left, find it's most-right.
        # If neither, we can just remove this node.
        last = None
        if right_child is not None:
            last = node_to_remove
            current = right_child
            while current.left is not None:
                last = current
                current = current.left
            # If first node is left-most, pop it in easy. Return.
            if last == node_to_remove:
                if node_that_points_to_removed_left_or_right == "left":
                    node_that_points_to_removed.left = current
                    current.left = node_to_remove.left
                elif node_that_points_to_removed_left_or_right == "right":
                    node_that_points_to_removed.right = current
                    current.left = node_to_remove.left
                return root
            # If left-most is lower, handle organization.
            else:
                if node_that_points_to_removed_left_or_right == "left":
                    node_that_points_to_removed.left = current
                    current.left = node_to_remove.left
                elif node_that_points_to_removed_left_or_right == "right":
                    node_that_points_to_removed.right = current
                    current.left = node_to_remove.left
                # Set right-most of this branch's right pointer to the
                # right-child of the removed node.
                last.left = None
                temp_right_most = current
                while temp_right_most.right is not None:
                    temp_right_most = temp_right_most.right
                temp_right_most.right = node_to_remove.right
                return root
        # Do this mirrored for the left.
        last = None
        if left_child is not None:
            last = node_to_remove
            current = left_child
            while current.right is not None:
                last = current
                current = current.right
            # If first node is right-most, pop it in easy. Return.
            if last == node_to_remove:
                if node_that_points_to_removed_left_or_right == "left":
                    node_that_points_to_removed.left = current
                    current.right = node_to_remove.right
                elif node_that_points_to_removed_left_or_right == "right":
                    node_that_points_to_removed.right = current
                    current.right = node_to_remove.right
                return root
            # If right-most is lower, handle organization.
            else:
                if node_that_points_to_removed_left_or_right == "left":
                    node_that_points_to_removed.left = current
                    current.right = node_to_remove.right
                elif node_that_points_to_removed_left_or_right == "right":
                    node_that_points_to_removed.right = current
                    current.right = node_to_remove.right
                # Set left-most of this branch's left pointer to the
                # left-child of the removed node.
                last.right = None
                temp_left_most = current
                while temp_left_most.left is not None:
                    temp_left_most = temp_left_most.left
                temp_left_most.left = node_to_remove.left
                return root

        # If node to remove has no children, just remove it.
        if left_child is None and right_child is None:
            if node_that_points_to_removed_left_or_right == "left":
                node_that_points_to_removed.left = None
            elif node_that_points_to_removed_left_or_right == "right":
                node_that_points_to_removed.right = None
            return root
