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

    def pair_sum(self, head: ListNode) -> int:
        """
        Find the maximum pair sum in the linked-list.

        Args:
            `head`: The beginning node of the linked-list.
        Returns:
            `max_pair_sum`: The maximum value of pair-sums.
        """

        # Edge-case
        # - 2 nodes
        if head.next.next is None:
            return head.val + head.next.val

        # Setup a reversed list to look at each two needed values at once.
        middle_node = self.find_middle_node(head)
        reversed_last_half = self.reverse_list(middle_node)
        max_pair_sum = 0

        # Iterate and compare to the maximum sum found.
        left_ptr = head
        right_ptr = reversed_last_half
        while right_ptr is not None:
            current_sum = left_ptr.val + right_ptr.val
            if current_sum > max_pair_sum:
                max_pair_sum = current_sum
            right_ptr = right_ptr.next
            left_ptr = left_ptr.next
        return max_pair_sum

    def reverse_list(self, head: ListNode) -> ListNode:
        """
        Return a newly created reversed version of the given linked-list.

        Args:
            `head`: The beginning node of the linked-list.
        Returns:
            `new_last_ptr`: The new beginning node of a linked-list.
        """

        # Edge-case:
        # - 2 nodes
        if head.next.next is None:
            new_head = ListNode(head.next.val)
            new_tail = ListNode(head.val)
            new_head.next = new_tail
            return new_head

        # Iterate forward through the list while changing the direction of the
        # next pointers.
        new_tail = ListNode(head.val)
        ptr = head.next
        new_last_ptr = new_tail
        while ptr is not None:
            new_node = ListNode(ptr.val)
            new_node.next = new_last_ptr
            new_last_ptr = new_node
            ptr = ptr.next

        # Return the new head
        return new_last_ptr

    def find_middle_node(self, head: ListNode) -> ListNode:
        """
        Return the pointer to the middle node. On even list, this is one to the right of center.

        Args:
            `head`: The beginning pointer.
        Returns:
            `slow_ptr`: The middle node.
        """

        # Use a fast and slow pointer to find the middle.
        slow_ptr = head
        fast_ptr = head
        while fast_ptr is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr
