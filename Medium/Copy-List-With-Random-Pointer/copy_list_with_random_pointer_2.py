from node import Node


class Solution:

    def copy_random_list_2(self, head: Node) -> Node:
        if not head:
            return None

        def clone_interleve():
            itr = head
            while itr:
                clone = Node(itr.val, itr.next, None)
                itr.next = clone
                itr = clone.next

        def set_random():
            itr = head
            while itr:
                clone = itr.next
                if itr.random:
                    clone.random = itr.random.next
                itr = clone.next

        def decouple():
            cloneHead = head.next
            cloneTail = head.next
            while cloneTail.next:
                cloneTail.next = cloneTail.next.next
                cloneTail = cloneTail.next
            return cloneHead

        clone_interleve()
        set_random()
        return decouple()
