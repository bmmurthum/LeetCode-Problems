""" Module to find if a linked-list has any cycles. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201

from node import Node


class Solution:
    """Problem given by LeetCode."""

    def copy_random_list(self, head: Node) -> Node:
        """
        Copies a linked list to a new set of nodes retaining their pointers to relative new nodes.

        Args:
            `head`: A pointer to the head of a linked list.
        Returns:
            `new_head`: A pointer to the head of new linked list.
        """

        # Handle empty node case
        if head is None:
            return None

        # Create list of old nodes
        old_list = []
        new_list = []
        ptr = head
        while ptr is not None:
            old_list.append(ptr)
            new_list.append(None)
            ptr = ptr.next

        # Create the new nodes, with val and next.
        new_list[len(old_list) - 1] = Node(old_list[len(old_list) - 1].val)
        for i in range(len(old_list) - 2, -1, -1):
            new_node = Node(old_list[i].val)
            new_list[i] = new_node
            if i < len(old_list) - 1:
                new_node.next = new_list[i + 1]

        # Look through old nodes' random-pointers and compare against list for
        # "indexes" to use for new nodes.
        ptr = head
        ptr_b = new_list[0]
        while ptr is not None:
            if ptr.random is not None:
                index = old_list.index(ptr.random)
                ptr_b.random = new_list[index]
            ptr = ptr.next
            ptr_b = ptr_b.next

        return new_list[0]

    def confirm_as_deepcopy(self, a: Node, b: Node) -> bool:
        """Confirms two linked-lists as deep copies of one another."""

        # Build lists for "a"
        a_list = []
        a_node_list = []
        while a is not None:
            a_list.append([a.val, a.random])
            a_node_list.append(a)
            a = a.next

        # Build lists for "b"
        b_list = []
        b_node_list = []
        while b is not None:
            b_list.append([b.val, b.random])
            b_node_list.append(b)
            b = b.next

        # Check lengths being the same.
        if len(a_list) != len(b_list):
            return False

        # Are any items of "b" shared with "a"?
        for node in b_node_list:
            if node in a_node_list:
                return False
        for node in a_node_list:
            if node in b_node_list:
                return False

        # Are the values and randoms the same for each node?
        for node_a, node_b in zip(a_list, b_list):
            if node_a[0] != node_b[0]:
                return False
            if node_a[1] is None and node_b[1] is None:
                continue
            elif (node_a[1] is not None and node_b[1] is None) or (
                node_a[1] is None and node_b[1] is not None
            ):
                return False
            else:
                a_random_index = a_node_list.index(node_a[1])
                b_random_index = b_node_list.index(node_b[1])
                if a_random_index != b_random_index:
                    return False

        return True


# a = Node(7)
# b = Node(13)
# c = Node(11)
# d = Node(10)
# e = Node(1)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# b.random = a
# c.random = e
# d.random = c
# e.random = a

# a = None

# result = Solution().copy_random_list(a)
# print("Done.")

# is_deepcopy = Solution().confirm_as_deepcopy(a, result)
# print(f"is_deepcopy(): {is_deepcopy}")

# Confirm as deep copy.
#  - Confirm no nodes are shared between linked lists
#  - Confirm vals and randoms are the same
