"""Module for testing function time performance"""

import timeit

NUM_TESTS = 500


# My solution
MYSETUP = """
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotate_right_1(self, head: ListNode, k: int) -> ListNode:
        if k == 0:  # No rotation
            return head
        if head is None:  # No head
            return None
        if head.next is None:  # One item
            return head
        if k == 1:  # If rotation is 1
            ptr = head
            while ptr.val is not None:
                if ptr.next.next is None:
                    ptr.next.next = head
                    new_head = ptr.next
                    ptr.next = None
                    break
                ptr = ptr.next
            return new_head
        new_list_tail = ListNode(None, None)
        new_list_head = ListNode(head.val, new_list_tail)
        ptr = head.next
        new_list_tail.val = ptr.val
        new_list_tail.next = None
        new_list_len = 2
        length = 2
        ptr = ptr.next
        # Starting with ptr at the third node
        while ptr is not None:
            length += 1
            # If haven't reached k length in new_list, add to tail
            if new_list_len < k:
                new_list_tail.next = ListNode(None, None)
                new_list_tail = new_list_tail.next
                new_list_tail.val = ptr.val
                new_list_tail.next = None
                new_list_len += 1
            else:
                # Add to tail
                new_list_tail.next = ListNode(None, None)
                new_list_tail = new_list_tail.next
                new_list_tail.val = ptr.val
                new_list_tail.next = None
                # Disconnect next and move head
                t = new_list_head.next
                new_list_head.next = None
                new_list_head = t
            ptr = ptr.next
        if k == length:
            return head
        elif k < length:
            remove_link_at = length - k
            new_list_tail.next = head
            for _ in range(1, remove_link_at):
                head = head.next
            head.next = None
            return new_list_head
        elif k % length == 0:
            return head
        else:
            remove_link_at = length - (k % length)
            ptr = head
            for _ in range(1, remove_link_at):
                ptr = ptr.next
            temp_ptr = ptr.next
            new_head = temp_ptr
            ptr.next = None
            while temp_ptr.next is not None:
                temp_ptr = temp_ptr.next
            temp_ptr.next = head
            return new_head
    def find(self, head):
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1
        return (length, temp)
    def getNewTail(self, head, idx):
        temp = head
        while idx != 1:
            temp = temp.next
            idx -= 1
        return temp
    def rotate_right_2(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length, tail = self.find(head)
        k = k % length
        if k == 0:
            return head
        tail.next = head
        new_tail = self.getNewTail(head, length - k)
        head = new_tail.next
        new_tail.next = None
        return head
sol = Solution()
x = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
y = 23
"""
MYCODE = """
RESULT = sol.rotate_right_1(x,y)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate_right_1():" + TIME_PER_RUN)


# Someone else's solution
MYCODE = """
RESULT = sol.rotate_right_2(x,y)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate_right_2():" + TIME_PER_RUN)
