""" Module to find if a linked-list has any cycles. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201

from list_node import ListNode


class Solution:
    """Problem given by LeetCode."""

    def has_cycle(self, head: ListNode) -> bool:
        """
        Tells us if a linked-list has a cycle.

        Args:
            `head`: A pointer to the head of a linked list.
        Returns:
            `True/False`: If the linked-list contains any cycles.
        """

        # Handle none-case and single-item-no-next-case
        if head is None or head.next is None:
            return False

        # Using fast-slow stepper to look for if they ever point to same node.
        fast = head.next
        slow = head
        while fast.next is not None and fast.next.next is not None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
