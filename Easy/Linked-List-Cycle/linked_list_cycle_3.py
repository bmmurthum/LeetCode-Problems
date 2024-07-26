from list_node import ListNode


class Solution:

    def has_cycle_3(self, head: ListNode) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False
