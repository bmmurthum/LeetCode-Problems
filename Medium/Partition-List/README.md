# Rotate List

**Description:**

Given the `head` of a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`.

You should preserve the original relative order of the nodes in each of the two partitions.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition_1(self, head: ListNode, x: int) -> ListNode:
        # ...
```

**Example:**

```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Input: head = [2,1], x = 2
Output: [1,2]
```

## Overview

For my solution, we're going to create two linked-lists at `a_head` and `b_head`, one for each condition of being above or below `x`. We'll keep track of their tails and some conditions while iterating.

1. We handle some edge cases upfront to avoid having to handle that logic internally in the loop.
2. While in the loop we add a value to the `a_head`/`b_head` if there isn't one yet, and amend a `a_tail`/`b_tail` if there isn't one yet.
3. Then we append to the `a_tail`/`b_tail` of each list as we go through the initial list `head`.
4. At the end we merge the two lists by making `a_tail.next = b_head`.
   - Just before this, we handle unique conditions of all in one list or the other, etc. 

```python
def partition_1(self, head: ListNode, x: int) -> ListNode:
    """
    Given a `head` of a linked-list, partition the list such that any nodes
    with a `val` less than `x` come before the others. Preserve relative
    order.

    Args:
        `head`: A ListNode object that is the head of a linked-list.
        `x`: An integer that guides the re-ordering of this method.
    Returns:
        `new_head`: A ListNode object that is the new head of a ordered
        linked-list.
    """

    # Handle edge-cases
    if head is None:
        return None
    if head.next is None:
        return head

    # Setup partitions
    a_tail = None
    a_head = ListNode(None, a_tail)
    a_empty = True
    a_empty_tail = True
    b_tail = None
    b_head = ListNode(None, b_tail)
    b_empty = True
    b_empty_tail = True

    # Look through list
    while head is not None:
        if head.val < x:
            if a_empty:
                a_head.val = head.val
                a_empty = False
            elif a_empty_tail:
                a_tail = ListNode(head.val, None)
                a_head.next = a_tail
                a_empty_tail = False
            else:
                a_tail.next = ListNode(head.val, None)
                a_tail = a_tail.next
        else:
            if b_empty:
                b_head.val = head.val
                b_empty = False
            elif b_empty_tail:
                b_tail = ListNode(head.val, None)
                b_head.next = b_tail
                b_empty_tail = False
            else:
                b_tail.next = ListNode(head.val, None)
                b_tail = b_tail.next
        head = head.next
    # If particular lists are full or empty, consider
    if a_head.val is None:
        return b_head
    elif b_head.val is None:
        return a_head
    elif a_head.next is None:
        a_head.next = b_head
    else:
        a_tail.next = b_head
    return a_head
```


## Tests

**Unit Testing**

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and straining the range of values written in constraints. We checked for:
- Zero items 
- One item
- Two items, to be sorted
- Two items, already correct
- All above `x`, all below `x`
- All items and `x` being the same value
- All items negative
- Only one item in first partition


**Code Coverage**

We received 100% code coverage on each tested method from the unit-test using the `coverage.py` tool.

```
> coverage run unit_test.py
> coverage report -m 
Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
partition_list.py      84      0   100%
unit_test.py          134      0   100%
-------------------------------------------------
TOTAL                 218      0   100%
```


**Memory Usage Testing**

I used `tracemalloc` to look at peak memory block usage during the running of three similar solutions on a 6 item case. We compare my solution with two other peoples', seen below.

Memory blocks used:

- `partition_1()`: 1472 blocks
- `partition_2()`: 312 blocks
- `partition_3()`: 176 blocks


**Process Time Testing**

I used `timeit` to isolate the individual functions on the same input.

- `partition_1()`: 8.114 x 10^-7 sec
- `partition_2()`: 3.870 x 10^-7 sec
- `partition_3()`: 4.632 x 10^-7 sec


## Reflections

The memory usage difference between my solution and the others is notable. It can't just be those helper variables I had, could it? I thinking maybe each pointed `ListNode` keeps the values of their children, or maybe garbage collection is involved.

These alternative solutions' speed is involved in their reducing logic in the loop and less memory calls I presume.  

## Solution Variations

`312 memory blocks` & `3.87 x 10^-7 sec`

```python
# Someone else's solution
def partition_2(self, head: ListNode, x: int) -> ListNode:

    less_head = ListNode()
    greater_head = ListNode()
    less = less_head
    greater = greater_head

    while head:
        if head.val < x:
            less.next = head
            less = less.next
        else:
            greater.next = head
            greater = greater.next
        head = head.next
    greater.next = None
    less.next = greater_head.next
    return less_head.next
```

`176 memory blocks` & `4.632 x 10^-7 sec`

```python
# Someone else's solution
def partition_3(self, head: ListNode, x: int) -> ListNode:

    less_head = ListNode()
    greater_head = ListNode()
    less = less_head
    greater = greater_head

    while head:
        if head.val < x:
            less.next = head
            less = less.next
        else:
            greater.next = head
            greater = greater.next
        head = head.next
    greater.next = None
    less.next = greater_head.next
    return less_head.next
```