"""Module for testing function time performance"""

import timeit

NUM_TESTS = 1000

# My solution
MYSETUP = """
class ListNode:
    def __init__(self, val=0, next=None):  # pylint: disable=W0622
        self.val = val
        self.next = next
class Solution:
    def mergetwolists_1(self, list1: ListNode, list2: ListNode) -> ListNode:
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
"""
MYCODE = """
a = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4))))))
b = ListNode(1, ListNode(1, ListNode(1)))
s = Solution()
c = s.mergetwolists_1(a, b)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("mergetwolists_1():" + TIME_PER_RUN)


# mergetwolists_2()
MYSETUP = """
class ListNode:
    def __init__(self, val=0, next=None):  # pylint: disable=W0622
        self.val = val
        self.next = next
class Solution:
    def mergetwolists_2(self, list1: ListNode, list2: ListNode) -> ListNode:
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
"""
MYCODE = """
a = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4))))))
b = ListNode(1, ListNode(1, ListNode(1)))
s = Solution()
c = s.mergetwolists_2(a, b)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("mergetwolists_2():" + TIME_PER_RUN)


# mergetwolists_3()
MYSETUP = """
class ListNode:
    def __init__(self, val=0, next=None):  # pylint: disable=W0622
        self.val = val
        self.next = next
class Solution:
    def mergetwolists_3(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 or not list2:
            return list1 if list1 else list2
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = self.mergetwolists_3(list1.next, list2)
        return list1
"""
MYCODE = """
a = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4))))))
b = ListNode(1, ListNode(1, ListNode(1)))
s = Solution()
c = s.mergetwolists_3(a, b)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("mergetwolists_3():" + TIME_PER_RUN)
