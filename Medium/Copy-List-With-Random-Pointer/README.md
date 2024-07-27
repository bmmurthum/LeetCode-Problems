# Copy List with Random Pointer

**Description:**

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return the `head` of the copied linked list.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will only be given the `head` of the original linked list.

**Constraints:**

- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or is pointing to some node in the linked list.

**Examples:**

```text
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

## Overview

```python
from node import Node
class Solution:
    """Problem given by LeetCode."""

    def copy_random_list(self, head: Node) -> Node:
        """
        Copies a linked list to a new set of nodes retaining their pointers to relative new nodes.

        Args:
            `head`: A pointer to the head of a linked list.
        Returns:
            `new_head`: A pointer to the head of new linked list.
        """

        # Handle empty node case
        if head is None:
            return None

        # Create list of old nodes
        old_list = []
        new_list = []
        ptr = head
        while ptr is not None:
            old_list.append(ptr)
            new_list.append(None)
            ptr = ptr.next

        # Create the new nodes, with val and next.
        new_list[len(old_list) - 1] = Node(old_list[len(old_list) - 1].val)
        for i in range(len(old_list) - 2, -1, -1):
            new_node = Node(old_list[i].val)
            new_list[i] = new_node
            if i < len(old_list) - 1:
                new_node.next = new_list[i + 1]

        # Look through old nodes' random-pointers and compare against list for
        # "indexes" to use for new nodes.
        ptr = head
        ptr_b = new_list[0]
        while ptr is not None:
            if ptr.random is not None:
                index = old_list.index(ptr.random)
                ptr_b.random = new_list[index]
            ptr = ptr.next
            ptr_b = ptr_b.next
        return new_list[0]
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We wrote a method `confirm_as_deepcopy()` that confirms the new linked list as a deep-copy, in that each item is uniquely new in memory while having values that would be parallel.

We checked for:

- LeetCode's three example cases.
- All node random pointers are `None`
- All random pointers are to the first node
- No nodes
- 15 nodes with assorted random pointing
- Single node, random pointer is `None`
- Single node, random pointer is to itself
- Two nodes
- Nodes having negative values, as seen in constraints

```text
** Unit Tests **

Unit Tests Ran: 10
Methods Tested: 3
Errors: 0
Skipped: 0
Failures: 9
```

`copy_list_with_random_pointer_2.py` works as submitted to LeetCode, but in validating it with my `confirm_as_deepcopy()` in the unit tests, it throws failure. When I ran a failed test case on it manually in debugging, we can see that the returned linked-list uses the same nodes as passed to it. Thus, not a deep-copy.

### Code Coverage

We received 100% code coverage on all methods with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report -m
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
call_tests.py                           13      0   100%
copy_list_with_random_pointer.py        60      5    92%
copy_list_with_random_pointer_2.py      28      0   100%
copy_list_with_random_pointer_3.py      24      0   100%
memory_tests.py                         48      0   100%
node.py                                  5      0   100%
testcases.py                           114      0   100%
time_tests.py                           42      0   100%
unit_tests.py                          124      0   100%
--------------------------------------------------------
TOTAL                                  458      5    99%
```

The missing coverage in `copy_list_with_random_pointer.py` is in the `confirm_as_deepcopy()` method in portions that we're not interested in checking. It would only be exercised on faulty cases.

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests **

Testcase 7: 15-long linked-list.
      copy_random_list(): 115688 blocks
    copy_random_list_2(): 98688 blocks
    copy_random_list_3(): 98136 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a couple test cases. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Testcase 7: 15-long linked-list.
      copy_random_list() runtime: 9.3262e-03 sec
    copy_random_list_2() runtime: 1.0881e-01 sec
    copy_random_list_3() runtime: 3.3911e-01 sec
```

## Reflections

The Olympics are happening in Paris right now. I did a skateboard of a trail near my house today.

## Solution Variations

### copy_list_with_random_pointer_2.py

Again, this is faulty and does not meet requirements. This returns a linked-list with some of the initial node memory addresses involved.

```python
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
```

### copy_list_with_random_pointer_3.py

```python
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
```
