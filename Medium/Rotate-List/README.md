# Rotate List

**Description:**

Given the `head` of a linked list, rotate the list to the right by `k` places.

- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 109`

**Example:**

```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

## Overview

We're iterating through a linked-list of `ListNode` with only tails and values. For this we build a combination of pointers and counters to later edit the list. The requirements call for us to return a `ListNode` that is the head of the new list.

There's a handful of unique cases that can be handled early:
- No rotation returns the initial `head`
- No head `ListNode` returns `None`
- One item, return the initial `head`
- Rotation of `1` can be handled more efficiently a different way

For our solution, we set up a new linked-list of `ListNode`. We create an initial two nodes, `new_list_head` and `new_list_tail` that are connected. We'll be using `ptr` to walk through the initial list. We'll also be keeping track of the `length` of the initial list and our `new_list_length` which we grow and maintain as a new list that becomes the length of rotation `k`.

1. We step through the initial list while `ptr` is valid.
2. While the `new_list_length` is less than the rotation `k` amount, we add nodes to that list.
3. Once the `new_list_length` matches `k`, we maintain it by removing from the head and adding at the tail.
4. When at the end of the initial list, we know the length and have a helping list of nodes.

If we see the rotation `k` is equal to `length`, the initial list is fine as is. `return head`

If the rotation amount `k` is less than the `length`, we put our new list as the beginning and put the initial list behind and remove the tail at the correct spot. `return new_list_head`

If the rotation `k` is greater than `length` and divisible by the `length`, the initial list is fine as is. `return head`

If the rotation `k` is greater than `length` and not-divisible, we do a similar cutting and mending as above.

```python
def rotate_right_1(self, head: ListNode, k: int) -> ListNode:
    """
    Given a linked-linked, rotate the list by some integer.
    Args:
        `head` - The head node that is connected to the others. No pointer to previous.
        `k` - The number of shifts to perform. If over total length, start at beginning again.

    """

    # Handling edge cases
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

    # k is the same as length, return original
    if k == length:
        return head
    # k is less
    elif k < length:
        remove_link_at = length - k
        new_list_tail.next = head
        for _ in range(1, remove_link_at):
            head = head.next
        head.next = None
        return new_list_head
    # k is more than length, and divisible by length
    elif k % length == 0:
        return head
    # k is more than length, and not-divisible by length
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
```

## Tests

**Unit Testing**

We implemented unit-tests for this problem with `import unittest`. We checked for:
- Simple case
- `None` as head given
- List of one node
- Rotation of 0 & 1
- Rotation same as length
- Rotation more & less than length
- Rotation more than and divisible by length

**Code Coverage**

We received 100% code coverage on each tested method from the unit-test using the `coverage.py` tool.

```
> coverage run unit_test.py
> coverage report -m 
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
rotate_list.py      93      0   100%
unit_test.py       144      0   100%
----------------------------------------------
TOTAL              237      0   100%
```

**Memory Usage Testing**

I used `tracemalloc` to look at peak memory block usage during the running of two similar functions on a 5 item case, rotated 23. We compare my solution with another person's, seen below.

Memory blocks used:

- `rotate_right_1()`: 1376 blocks
- `rotate_right_2()`: 48 blocks

**Process Time Testing**

I used `timeit` to isolate the individual functions on the same input.

My solution `rotate_right_1()`, is 35% faster than solution `rotate_right_2()`. I credit this to the creation of the temporary list that was made during iteration, but I'm not sure. It seems like their's also iterates the same amount.

- `rotate_right_1()`: 0.646 x 10^-7 sec
- `rotate_right_2()`: 1.010 x 10^-7 sec


## Reflections

My solution is pretty verbose, pretty overwritten. I'd like to try for a more elegant solution next time around. I'll try to be more open to helper methods for clarity.

When doing writing unit-tests I kept code-coverage over ming to inform cases. Running the coverage test I noticed that the other's solution have some logic that would never come to run, which we deleted.

## Solution Variations

Similar to mine, without the building of a list as iterating. I like their use of helping methods. Very readable.

```python
# Someone else's solution
def rotate_right_2(self, head: ListNode, k: int) -> ListNode:
    if not head:
        return head
    length,tail = self.find(head)
    k = k % length
    if k == 0:
        return head
    tail.next = head
    new_tail = self.getNewTail(head,length-k)
    head = new_tail.next
    new_tail.next = None
    return head

def find(self,head):
    if not head :
        return (0,None)
    length = 1
    temp = head
    while temp.next:
        temp = temp.next
        length += 1
    return (length,temp)

def getNewTail(self,head,idx):
    temp = head
    while idx != 1:
        temp = temp.next
        idx -= 1
    return temp
```