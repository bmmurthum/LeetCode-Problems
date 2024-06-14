""" This module holds a function to perform LRU operation """

# pylint: disable=W0622


class ListNode:
    """Created class to manipulate linked-links within hash-table"""

    #   Hash Table
    #   0 : Node(A) -> Node(C)
    #   1 : Node(B)
    #   2 :
    #   3 : Node(D)
    # A.hash_next == C
    # hash_table[0] == A
    # hash_table[2] == None

    #   LRU Linked-List
    #   A > B > C > D
    #   H           T
    # A.next == B
    # C.prev == B
    # D.next == None
    # head_ptr == A
    # tail_ptr == D

    def __init__(
        self,
        key: int,
        val: int,
        hash_value: int,
        prev=None,
        next=None,
        hash_next=None,
    ):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.hash_next = hash_next
        self.hash_value = hash_value


class LRUCache:
    """Given class by LeetCode to perform methods in"""

    #   Hash Table
    #   0 : Node(A) -> Node(C)
    #   1 : Node(B)
    #   2 :
    #   3 : Node(D)
    # A.hash_next == C
    # hash_table[0] == A
    # hash_table[2] == None

    #   LRU Linked-List
    #   A > B > C > D
    #   H           T
    # A.next == B
    # C.prev == B
    # D.next == None
    # head_ptr == A
    # tail_ptr == D

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_hash_table = 5
        self.multiplier_hash_table = 1
        self.hash_table = [None] * max(
            self.min_hash_table, int(self.capacity * self.multiplier_hash_table)
        )
        self.num_keys = 0
        self.head_ptr = None
        self.tail_ptr = None

    def remove_from_hash_table(self, node: ListNode) -> None:
        """
        Remove a given `ListNode` from the hash-table, and mend links in hash-table.

        Args:
          `ListNode`: A node containing `key` and `value` integrated into our hash-table.
        Returns:
          `None`
        """
        # If first value
        if self.hash_table[node.hash_value].key == node.key:
            self.hash_table[node.hash_value] = self.hash_table[
                node.hash_value
            ].hash_next
            return
        # If some value along linked-list
        ptr = self.hash_table[node.hash_value]
        while ptr.hash_next is not None:
            if ptr.hash_next.key == node.key:
                # temp = ptr.hash_next
                ptr.hash_next = ptr.hash_next.hash_next
                # del temp
                return
            ptr = ptr.hash_next

    def make_tail(self, node: ListNode, found_in_hash_map: bool) -> None:
        """
        Properly positions this `ListNode` in the linked-list of least-recently
        used order, and mends links. Does not remove `head`.

        We just added this Node to hash-map, put(), or retrieved it, get().
        This updates the LRU Linked-List.

        Args:
          `node`: A node containing `key` and `value` integrated into our hash-table.

          `found_in_hash_map`: Whether this `node` was seen in the hash-map.
        Returns:
          `None`
        """

        # If already stored
        if found_in_hash_map is True:
            # If the update is on the tail, return with no changes
            if self.tail_ptr == node:
                return
            # If the update is on the only item
            elif self.head_ptr == node and self.tail_ptr is None:
                return
            # If the update is on the head
            elif self.head_ptr == node:
                self.head_ptr = self.head_ptr.next
                self.head_ptr.prev = None
                self.tail_ptr.next = node
                node.prev = self.tail_ptr
                self.tail_ptr = node
                self.tail_ptr.next = None
                return
            # Head and tail already handled, this must be in middle.
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail_ptr.next = node
                node.prev = self.tail_ptr
                self.tail_ptr = node
                self.tail_ptr.next = None
                return
        # If not stored
        elif found_in_hash_map is False:
            # No items considered yet
            if self.head_ptr is None:
                self.head_ptr = node
                return
            # Second item looked at
            elif self.tail_ptr is None:
                self.tail_ptr = node
                self.tail_ptr.prev = self.head_ptr
                self.head_ptr.next = node
                return
            # If not first items, add to end.
            else:
                self.tail_ptr.next = node
                node.prev = self.tail_ptr
                self.tail_ptr = node

    def _hash(self, key: int):
        """
        Returns a hash int for this node to be stored. It considers a
        multiplier for the hash-table size for consideration of efficiency.
        """
        return hash((key * 3) / 2) % max(
            self.min_hash_table, int(self.capacity * self.multiplier_hash_table)
        )

    def get(self, key: int) -> int:
        """Returns the `value` of the `key` given."""

        # Look through the hash-table for key and handle LRU linked-list
        ptr = self.hash_table[self._hash(key)]
        if ptr is None:
            return -1
        elif ptr.key == key:
            self.make_tail(ptr, True)
            return ptr.val
        else:
            while ptr.hash_next is not None:
                if ptr.hash_next.key == key:
                    self.make_tail(ptr.hash_next, True)
                    return ptr.hash_next.val
                ptr = ptr.hash_next
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Adds the `key`-`value` pair to storage if not already there, updates the `value` otherwise.

        It removes the `head` from the LRU Linked List if needed.
        """

        # If this value doesn't exist at this first hash item, put one here
        ptr = self.hash_table[self._hash(key)]
        if ptr is None:
            ptr = ListNode(key, value, self._hash(key))
            self.hash_table[self._hash(key)] = ptr
            # Add to LRU consideration
            self.make_tail(ptr, False)
            # Increment number of keys
            if self.num_keys <= self.capacity:
                self.num_keys += 1
        # Look through nodes at this hash-value for our key
        else:
            # Check first node
            if ptr.key == key:
                # Update value
                ptr.val = value
                # Add to LRU consideration
                self.make_tail(ptr, True)
                return None
            else:
                found_key = False
                while ptr.hash_next is not None:
                    if ptr.hash_next.key == key:
                        found_key = True
                        # Update value
                        ptr.hash_next.val = value
                        # Add to LRU consideration
                        self.make_tail(ptr.hash_next, True)
                        break
                    ptr = ptr.hash_next
                if found_key is False:
                    # Did not find the key in list, add to hash list
                    ptr.hash_next = ListNode(key, value, self._hash(key))
                    # Add to LRU consideration
                    self.make_tail(ptr.hash_next, False)
                    # Increment number of keys
                    if self.num_keys <= self.capacity:
                        self.num_keys += 1

        # If at capacity, remove the head and change pointers
        if self.num_keys > self.capacity:
            self.head_ptr.next.prev = None
            temp = self.head_ptr
            self.head_ptr = self.head_ptr.next
            self.remove_from_hash_table(temp)
            self.num_keys = self.capacity
        return None
