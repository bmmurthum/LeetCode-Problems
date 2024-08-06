"""Class from LeetCode.com"""

# Ignore "Redefining built-in 'next'"
# pylint: disable=W0622


# Definition for singly-linked list.
class ListNode:
    """Class from LeetCode.com"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Class from LeetCode.com"""

    def reverse_list(self, head: ListNode) -> ListNode:
        """
        Return a reversed version of the given linked-list.

        Args:
            `head`: The beginning node of the linked-list.
        Returns:
            `ptr`: The new beginning node of the linked-list.
        """

        # Edge-cases:
        # - O / 1 / 2 nodes
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            second = head.next
            head.next = None
            second.next = head
            return second

        # Iterate forward through the list while changing the direction of the
        # next pointers.
        last_ptr = head
        ptr = head.next
        next_holder = head.next.next
        last_ptr.next = None
        while next_holder is not None:
            ptr.next = last_ptr
            last_ptr = ptr
            ptr = next_holder
            next_holder = next_holder.next
        ptr.next = last_ptr

        # Return the new head
        return ptr
