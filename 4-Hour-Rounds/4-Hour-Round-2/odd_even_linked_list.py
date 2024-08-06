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

    def odd_even_list(self, head: ListNode) -> ListNode:
        """
        Return a linked-list with all "odd-indexed" nodes together and
        "even-indexed" node together, keeping their relative order.

        This works in-place with O(1) extra space and O(n) time complexity.

        Args:
            `head`: The beginning node of the linked-list.
        Returns:
            `head`: The same node with changes.
        """

        # Edge-cases:
        # - O / 1 / 2 nodes
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            return head

        # Change all of the nexts.
        # On reaching end, append the evens to the end of odds.
        odd_ptr = head
        even_ptr = head.next
        even_head = head.next
        while True:
            if even_ptr.next is not None:
                odd_ptr.next = even_ptr.next
                odd_ptr = odd_ptr.next
            else:
                odd_ptr.next = even_head
                even_ptr.next = None
                break
            if odd_ptr.next is not None:
                even_ptr.next = odd_ptr.next
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = even_head
                even_ptr.next = None
                break

        # Return the changed linked-list.
        return head
