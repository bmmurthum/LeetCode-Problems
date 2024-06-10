""" Module to report peak-memory used by method """

import tracemalloc


class ListNode:
    """Defines a node object"""

    def __init__(self, val=0, next=None):  # pylint: disable=W0622
        self.val = val
        self.next = next


class Solution:
    """LeetCode's Solution Class"""

    # My solution
    def mergetwolists_1(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Returns a list of value-sorted nodes from two other lists. With recursion.
        """
        temp = ListNode(None, None)
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        if list1.val <= list2.val:
            temp.val = list1.val
            temp.next = self.mergetwolists_1(list1.next, list2)
        else:
            temp.val = list2.val
            temp.next = self.mergetwolists_1(list1, list2.next)
        return temp

    def mergetwolists_2(self, list1: ListNode, list2: ListNode) -> ListNode:
        """Someone else's solution"""
        if not list1:
            return list2
        if not list2:
            return list1
        merged_head = None
        merged_tail = None
        ptr1 = list1
        ptr2 = list2
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                if not merged_head:
                    merged_head = ptr1
                    merged_tail = merged_head
                else:
                    merged_tail.next = ptr1
                    merged_tail = merged_tail.next
                ptr1 = ptr1.next
            else:
                if not merged_head:
                    merged_head = ptr2
                    merged_tail = merged_head
                else:
                    merged_tail.next = ptr2
                    merged_tail = merged_tail.next
                ptr2 = ptr2.next
        if ptr1:
            merged_tail.next = ptr1
        else:
            merged_tail.next = ptr2
        return merged_head

    def mergetwolists_3(self, list1: ListNode, list2: ListNode) -> ListNode:
        """Someone else's solution"""
        if not list1 or not list2:
            return list1 if list1 else list2
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = self.mergetwolists_3(list1.next, list2)
        return list1


# Testing Memory Allocation
# mergetwolists_1()
a = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4))))))
b = ListNode(1, ListNode(1, ListNode(1)))
s = Solution()
tracemalloc.start()
c = s.mergetwolists_1(a, b)
TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("mergetwolists_1(): " + TRACED_MEMORY_PEAK + " blocks")


# Testing Memory Allocation
# mergetwolists_2()
a = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4))))))
b = ListNode(1, ListNode(1, ListNode(1)))
s = Solution()
tracemalloc.start()
c = s.mergetwolists_2(a, b)
TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("mergetwolists_2(): " + TRACED_MEMORY_PEAK + " blocks")


# Testing Memory Allocation
# mergetwolists_3()
a = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4))))))
b = ListNode(1, ListNode(1, ListNode(1)))
s = Solution()
tracemalloc.start()
c = s.mergetwolists_3(a, b)
TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("mergetwolists_3(): " + TRACED_MEMORY_PEAK + " blocks")
