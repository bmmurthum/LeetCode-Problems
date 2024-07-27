from node import Node


class Solution:

    def copy_random_list_3(self, head: Node) -> Node:
        if not head:
            return head
        node = head
        while node:
            new = Node(node.val)
            actualNext = node.next
            node.next = new
            new.next = actualNext
            node = actualNext
        curr = head
        while curr and curr.next:
            random = curr.random
            if random:
                new_random = random.next
                curr.next.random = new_random
            else:
                curr.next.random = None
            nxt = curr.next
            tmp = nxt.next
            nxt.next = nxt.next.next if nxt.next else None
            curr = tmp
        return head.next
