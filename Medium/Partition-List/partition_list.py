""" This module holds a function to rotate linked-lists """

# pylint: disable=W0622


# Definition for singly-linked list.
class ListNode:
    """Given class by LeetCode to manipulate linked-links"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Given class by LeetCode to perform methods in"""

    def partition_1(self, head: ListNode, x: int) -> ListNode:
        """
        Given a `head` of a linked-list, partition the list such that any nodes
        with a `val` less than `x` come before the others. Preserve relative
        order.

        Args:
          `head`: A ListNode object that is the head of a linked-list.
          `x`: An integer that guides the re-ordering of this method.
        Returns:
          `new_head`: A ListNode object that is the new head of a ordered
          linked-list.
        """

        # Handle edge-cases
        if head is None:
            return None
        if head.next is None:
            return head

        # Setup partitions
        a_tail = None
        a_head = ListNode(None, a_tail)
        a_empty = True
        a_empty_tail = True
        b_tail = None
        b_head = ListNode(None, b_tail)
        b_empty = True
        b_empty_tail = True

        # Look through list
        while head is not None:
            if head.val < x:
                if a_empty:
                    a_head.val = head.val
                    a_empty = False
                elif a_empty_tail:
                    a_tail = ListNode(head.val, None)
                    a_head.next = a_tail
                    a_empty_tail = False
                else:
                    a_tail.next = ListNode(head.val, None)
                    a_tail = a_tail.next
            else:
                if b_empty:
                    b_head.val = head.val
                    b_empty = False
                elif b_empty_tail:
                    b_tail = ListNode(head.val, None)
                    b_head.next = b_tail
                    b_empty_tail = False
                else:
                    b_tail.next = ListNode(head.val, None)
                    b_tail = b_tail.next
            head = head.next
        if a_head.val is None:
            return b_head
        elif b_head.val is None:
            return a_head
        elif a_head.next is None:
            a_head.next = b_head
        else:
            a_tail.next = b_head
        return a_head

    def partition_2(self, head: ListNode, x: int) -> ListNode:
        """Partition the linked list"""

        less_head = ListNode()
        greater_head = ListNode()
        less = less_head
        greater = greater_head

        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        greater.next = None
        less.next = greater_head.next
        return less_head.next

    def partition_3(self, head: ListNode, x: int) -> ListNode:
        """Partition the linked list"""
        if not head or not head.next:
            return head

        lessstart = ListNode()
        morestart = ListNode()
        less = lessstart
        more = morestart
        node = head

        while node:
            if node.val < x:
                less.next = node
                node = node.next
                less = less.next
                if less:
                    less.next = None
            else:
                more.next = node
                node = node.next
                more = more.next
                if more:
                    more.next = None

        less.next = morestart.next
        return lessstart.next
