# Linked List Cycle

**Description:**

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

**Constraints:**

- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked-list.

**Examples:**

```text
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## Overview

My solution uses two steppers, one going twice as fast, to see if they ever come to be at the same node at any point. If that's ever `True` we know there has been a cycle. It can end as soon as the faster stepper finds a `ListNode.next` is `None`.

```python
class ListNode:
    """Node definition given by LeetCode."""

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """Problem given by LeetCode."""

    def has_cycle(self, head: ListNode) -> bool:
        """
        Tells us if a linked-list has a cycle.

        Args:
            `head`: A pointer to the head of a linked list.
        Returns:
            `True/False`: If the linked-list contains any cycles.
        """

        # Handle none-case and single-item-no-next-case
        if head is None or head.next is None:
            return False

        # Using fast-slow stepper to look for if they ever point to same node.
        fast = head.next
        slow = head
        while fast.next is not None and fast.next.next is not None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We checked for:

- LeetCode's three example cases.
- A simple 5-long linked list with a cycle
- A 12-long linked-list without a cycle
- A 12-Long linked-list with a cycle
  - With positive/negative values held by nodes
- A single item in the linked-list, points to itself
- A single item with no cycle
- No items

```text
** Unit Tests **

Unit Tests Ran: 9
Methods Tested: 3
Errors: 0
Skipped: 0
Failures: 0
```

### Code Coverage

We received 100% code coverage on all methods with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report -m
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
call_tests.py               13      0   100%
linked_list_cycle.py        13      0   100%
linked_list_cycle_2.py      17      0   100%
linked_list_cycle_3.py      10      0   100%
list_node.py                 4      2    50%   8-9
memory_tests.py             84      0   100%
testcases.py               117      0   100%
time_tests.py               75      0   100%
unit_tests.py              116      0   100%
------------------------------------------------------
TOTAL                      449      2    99%
```

`list_node.py` is missing coverage only in that its a module called by others. We could exclude this from coverage.

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests **

Testcase 5: 12-long linked-list without cycle.
      has_cycle(): 64 blocks
    has_cycle_2(): 64 blocks
    has_cycle_3(): 792 blocks

Testcase 6: 12-long linked-list with cycle.
      has_cycle(): 64 blocks
    has_cycle_2(): 64 blocks
    has_cycle_3(): 792 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a couple test cases. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Testcase 5: 12-long linked-list without cycle.
      has_cycle() runtime: 1.2530e-04 sec
    has_cycle_2() runtime: 1.6240e-04 sec
    has_cycle_3() runtime: 2.5680e-04 sec

Testcase 6: 12-long linked-list with cycle.
      has_cycle() runtime: 2.2180e-04 sec
    has_cycle_2() runtime: 2.7150e-04 sec
    has_cycle_3() runtime: 2.9680e-04 sec
```

## Reflections

I'm happy with how this played out. No notes here.

I wish I had a notepad nearby.

## Solution Variations

### insert_interval_2.py

They have a similar idea to my solution, but is messier to look at.

```python
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
```

### insert_interval_3.py

Uses more memory and is slower. I can see the appeal of this solution in how clear it is.

```python
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
```
