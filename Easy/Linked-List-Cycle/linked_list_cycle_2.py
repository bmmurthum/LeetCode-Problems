from list_node import ListNode


class Solution:

    def has_cycle_2(self, head: ListNode) -> bool:
        if not head:
            return False
        current_node = head
        next_node = head.next
        if not current_node or not next_node:
            return False
        while current_node and next_node:
            if current_node == next_node:
                return True
            if not next_node.next or not next_node.next.next:
                break
            current_node = current_node.next
            next_node = next_node.next.next
        return False
