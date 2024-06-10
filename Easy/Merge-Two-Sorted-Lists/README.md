# Merge Two Sorted Lists

**Description:**

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

We're given this `ListNode` class to work with, to make objects for our linked lists.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

**Example:**

```
# (1) -> (2) -> (3)
a = ListNode(1, ListNode(2, ListNode(3)))
# (3) -> (4) -> (5)
b = ListNode(3, ListNode(4, ListNode(5)))
Input: mergetwolists(a,b)
Output: (1) -> (2) -> (3) -> (3) -> (4) -> (5)

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
```

## Overview

My solution recursively builds a new linked-list `temp` to return. It looks at two nodes' values (if not `None`) and makes the value of this `temp` node equal to the lower value node, then makes this `temp` node point to the result of this same function on (1) the `.next` value of the linked-list it took from and (2) the other list it did not.

This ends up returning the head node of a linked-list in order sorted by ascending order. 

```python
# My solution
def mergetwolists_1(self, list1: ListNode, list2: ListNode) -> ListNode:
    # Start with an empty node.
    temp = ListNode(None, None)
    # If THIS node is empty, return the other.
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    # If THIS node has the lower value, make this the value, then look to
    # compare the next one from this list and the same from the other list.
    if list1.val <= list2.val:
        temp.val = list1.val
        temp.next = self.mergetwolists_1(list1.next, list2)
    else:
        temp.val = list2.val
        temp.next = self.mergetwolists_1(list1, list2.next)
    return temp
```

## Tests

**Unit Testing**

We implemented for this problem with `import unittest`. Tests were made for:
- Simple 3-value and 4-value case
- One of the linked-lists being empty
- Both empty
- One linked-list having all single value in beginning
- Unordered linked-list, being handled badly
  - Method calls for ascending ordered lists


**Code Coverage**

We received 100% code coverage on `merge_two_sorted_lists.py` from the unit test using the `coverage.py` tool.

The missing unit-test coverage is conditions that were expected to not be met in the tests.

```
> coverage run unitTest.py
> coverage report -m 
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
merge_two_sorted_lists.py      17      0   100%
unit_test.py                  127     13    90%   42, 48, 74, 80, 105-108, 111-112, 138, 144, 176
---------------------------------------------------------
TOTAL                         144     13    91%
```

**Memory Usage Testing**

I used `tracemalloc` to look at peak memory block usage during the running of the function. We compare my solution with two other solutions, seen below.

My solution `mergetwolists_1()` more memory than was initially given. The other solutions did so, in place?

Memory blocks used:

- `mergetwolists_1()`: 1120 blocks
- `mergetwolists_2()`: 0 blocks
- `mergetwolists_3()`: 0 blocks


**Process Time Testing**

I used `timeit` to isolate the individual functions on the same input.

My solution `mergetwolists_1()` is 50% slower than the `mergetwolists_2()`. It must be in the creation/assignment of objects at each level of recursion.

- `mergetwolists_1()`: 1.449 x 10^-6 sec
- `mergetwolists_2()`: 0.946 x 10^-6 sec
- `mergetwolists_3()`: 0.985 x 10^-6 sec


## Reflections

I'm curious about whether a less than 100% unit-test coverage feels like a problem. I could rewrite the testing logic into a reused method that gets called on.

## Solution Variations

These other two solutions are very close to same performance. `mergetwolists_3()` feels easier to read and doesn't require logic for a tail.

`mergetwolists_2()` opts for iterating through the lists with pointers as it builds its new linked-list. I'm surprised the `merged_head` doesn't use the same memory requirements as my solution. It could be that `tracemalloc` has a different consideration for recursive functions than I understand.

`0 memory blocks` & `0.946 x 10^-6 sec`
```python
# Someone else's solution
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
```

`0 memory blocks` & `0.985 x 10^-6 sec`
```python
# Someone else's solution
def mergetwolists_3(self, list1: ListNode, list2: ListNode) -> ListNode:
    if not list1 or not list2:
        return list1 if list1 else list2
    if list1.val > list2.val:
        list1, list2 = list2, list1
    list1.next = self.mergetwolists_3(list1.next, list2)
    return list1
```