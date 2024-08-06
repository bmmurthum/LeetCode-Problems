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

    def delete_middle(self, head: ListNode) -> ListNode:
        """
        Return the linked-list with the "middle-index" node removed.

        Args:
            `head`: The node that is the beginning of the list.
        Returns:
            `head`: The same node of before.
        """

        # Count the length of the list
        count = 0
        ptr = head
        while ptr is not None:
            count += 1
            ptr = ptr.next

        # If only one item in linked-list
        if count == 1:
            return None

        # Iterate through for the halfway item and remove
        target = count // 2
        count = 1
        ptr = head.next
        last = head
        while ptr is not None:
            if count == target:
                last.next = ptr.next
                break
            count += 1
            ptr = ptr.next
            last = last.next

        # Return head
        return head
